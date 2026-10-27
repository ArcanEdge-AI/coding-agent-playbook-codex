"""Check claim dispositions and literal reader excerpts; not semantic correctness."""
import argparse
from collections import Counter
import json
from pathlib import Path


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def inspect(root, claim_paths, treatment_path, readers, coverage_paths):
    errors, claims, treatments = [], [], []

    def read_array(path):
        try:
            value = json.loads(path.read_text(encoding='utf-8'))
            if isinstance(value, list):
                return value
            errors.append(f'{path.name}: expected a JSON array')
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            errors.append(f'{path.name}: {exc}')
        return []

    def reader_path(name):
        if not nonempty(name) or Path(name).is_absolute():
            errors.append(f'Invalid relative reader path: {name!r}')
            return None
        path = (root / name).resolve()
        if not path.is_relative_to(root) or not path.is_file() or path.suffix.lower() != '.md':
            errors.append(f'Reader outside root, missing or not Markdown: {name}')
            return None
        if path in {p.resolve() for p in [*coverage_paths, *claim_paths, treatment_path]}:
            errors.append(f'An audit/index cannot be a reader: {name}')
            return None
        return path

    allowed = {}
    for name in readers:
        path = reader_path(name)
        if path is not None:
            try:
                allowed[name] = path.read_text(encoding='utf-8')
            except (OSError, UnicodeError) as exc:
                errors.append(f'{name}: {exc}')
    for path in claim_paths:
        claims.extend(read_array(path))
    treatments = read_array(treatment_path)
    units = []
    for path in coverage_paths:
        units.extend(read_array(path))

    def keyed(rows, kind):
        result = {}
        for row in rows:
            if not isinstance(row, dict) or not nonempty(row.get('id')):
                errors.append(f'{kind}: each row needs a nonempty id')
                continue
            ident = row['id']
            if ident in result:
                errors.append(f'Duplicate {kind} id: {ident}')
            result[ident] = row
        return result

    by_id = keyed(claims, 'claim')
    by_treatment = keyed(treatments, 'treatment')
    by_unit = keyed(units, 'unit')
    inspections = {'inspected', 'partial', 'pending', 'inaccessible', 'excluded', 'not_applicable'}
    for ident, row in by_unit.items():
        if not nonempty(row.get('task')):
            errors.append(f'{ident}: unit task required')
        for key in ('sources', 'audiences'):
            if not isinstance(row.get(key), list) or not row[key] or not all(nonempty(x) for x in row[key]):
                errors.append(f'{ident}: nonempty unit {key} list required')
        state = row.get('inspection')
        if not isinstance(state, str) or state not in inspections:
            errors.append(f'{ident}: invalid inspection')
        if state != 'inspected' and not nonempty(row.get('reason')):
            errors.append(f'{ident}: inspection reason required')
        ids = row.get('claim_ids')
        if not isinstance(ids, list) or not all(nonempty(x) for x in ids):
            errors.append(f'{ident}: claim_ids must be a string list')
            continue
        if len(ids) != len(set(ids)):
            errors.append(f'{ident}: duplicate claim_ids')
        if state == 'inspected' and not ids:
            errors.append(f'{ident}: inspected unit needs claims')
        for claim_id in ids:
            if claim_id not in by_id:
                errors.append(f'{ident}: unknown claim {claim_id}')
    for ident, row in by_id.items():
        for key in ('claim', 'unit_id', 'facet', 'condition', 'outcome'):
            if not nonempty(row.get(key)):
                errors.append(f'{ident}: {key} required')
        if not isinstance(row.get('qualifier'), str):
            errors.append(f'{ident}: qualifier must be a string (may be empty)')
        owner = row.get('unit_id')
        unit = by_unit.get(owner) if isinstance(owner, str) else None
        if unit is None:
            errors.append(f'{ident}: unknown canonical unit')
        elif not isinstance(unit.get('claim_ids'), list) or ident not in unit['claim_ids']:
            errors.append(f'{ident}: absent from canonical unit claim_ids')
        for key in ('sources', 'audiences'):
            if not isinstance(row.get(key), list) or not row[key] or not all(nonempty(x) for x in row[key]):
                errors.append(f'{ident}: nonempty {key} list required')
    for ident in sorted(by_id.keys() - by_treatment.keys()):
        errors.append(f'Missing treatment: {ident}')
    for ident in sorted(by_treatment.keys() - by_id.keys()):
        errors.append(f'Unknown treatment id: {ident}')

    counts, excerpts = Counter(), 0
    for ident, row in by_treatment.items():
        status = row.get('status')
        if not isinstance(status, str) or status not in {'documented', 'partial', 'excluded', 'disputed'}:
            errors.append(f'{ident}: invalid status')
            continue
        counts[status] += 1
        if status == 'documented' and not nonempty(row.get('reader_check')):
            errors.append(f'{ident}: specific semantic reader_check required')
        if status != 'documented' and not nonempty(row.get('reason')):
            errors.append(f'{ident}: specific reason required')
        file, excerpt = row.get('reader_file'), row.get('reader_excerpt')
        if status == 'documented' or file is not None or excerpt is not None:
            if not nonempty(file) or file not in allowed:
                errors.append(f'{ident}: reader_file must name an explicit allowed reader')
            elif not nonempty(excerpt) or excerpt not in allowed[file]:
                errors.append(f'{ident}: exact reader_excerpt absent from {file}')
            else:
                excerpts += 1
    if not by_id:
        errors.append('No claims supplied')
    if not by_unit:
        errors.append('No coverage units supplied')
    unit_statuses = {}
    for ident, row in by_unit.items():
        ids = row.get('claim_ids')
        if row.get('inspection') in ('excluded', 'not_applicable'):
            unit_statuses[ident] = 'excluded'
        elif (row.get('inspection') == 'inspected' and isinstance(ids, list) and ids
              and all(isinstance(x, str) and x in by_id and by_treatment.get(x, {}).get('status') == 'documented' for x in ids)):
            unit_statuses[ident] = 'indexed'
        else:
            unit_statuses[ident] = 'partial'
    return {
        'coverage_units': len(by_unit), 'unit_statuses': unit_statuses,
        'open_units': [ident for ident, state in unit_statuses.items() if state == 'partial'],
        'units_requiring_source_closure_review': [ident for ident, state in unit_statuses.items() if state == 'indexed'],
        'claims': len(by_id), 'treatments': len(by_treatment), 'statuses': dict(counts),
        'reader_files': len(allowed), 'exact_excerpts_found': excerpts, 'errors': errors,
        'mechanical_passed': not errors,
        'open_contracts': [ident for ident, row in by_treatment.items()
                           if row.get('status') in ('partial', 'disputed')],
        'limits': 'Indexed means selected children are accounted for, not that a unit is documented or complete. Source-first closure must check unindexed branches/fields and atomicity. This helper does not validate source locators; use check_source_paths.py --records for all claim and unit files. Matching excerpts do not establish semantic acceptance.',
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--docs-root', required=True, type=Path)
    parser.add_argument('--claims', required=True, nargs='+', type=Path)
    parser.add_argument('--coverage', required=True, nargs='+', type=Path)
    parser.add_argument('--treatments', required=True, type=Path)
    parser.add_argument('--readers', required=True, nargs='+')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    root = args.docs_root.resolve()
    if not root.is_dir():
        parser.error('docs-root must exist')
    if args.output:
        output = args.output.resolve()
        protected = {p.resolve() for p in [*args.coverage, *args.claims, args.treatments]}
        protected.update((root / name).resolve() for name in args.readers)
        if not output.is_relative_to(root) or output in protected:
            parser.error('output must be within docs-root and cannot overwrite an input/reader')
    result = inspect(root, args.claims, args.treatments, args.readers, args.coverage)
    encoded = json.dumps(result, indent=2) + '\n'
    if args.output:
        args.output.write_text(encoded, encoding='utf-8')
    print(encoded, end='')
    raise SystemExit(0 if result['mechanical_passed'] else 1)


if __name__ == '__main__':
    main()
