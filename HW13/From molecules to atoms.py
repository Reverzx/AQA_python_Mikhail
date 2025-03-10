import re


def from_molecules_to_atoms(formula):
    formula = formula.replace('[', '(').replace(']', ')').replace('{', '(').replace('}', ')')

    def parse_group(subformula, multiplier=1):
        counts = {}
        for element, number in re.findall(r"([A-Z][a-z]?)(\d*)", subformula):
            count = int(number) if number else 1
            counts[element] = counts.get(element, 0) + count * multiplier
        return counts

    while '(' in formula:
        match = re.search(r"\(([^()]+)\)(\d*)", formula)
        if not match:
            break

        subformula, factor = match.groups()
        factor = int(factor) if factor else 1

        parsed_counts = parse_group(subformula, factor)
        replacement_str = "".join(f"{el}{cnt}" for el, cnt in parsed_counts.items())

        formula = formula[:match.start()] + replacement_str + formula[match.end():]

    return parse_group(formula)


print(from_molecules_to_atoms("K4[ON(SO3)2]2"))
print(from_molecules_to_atoms("H2O"))
print(from_molecules_to_atoms("Mg(OH)2"))
assert from_molecules_to_atoms("K4[ON(SO3)2]2") == {'O': 14, 'N': 2, 'S': 4, 'K': 4}
assert from_molecules_to_atoms("H2O") == {'H': 2, 'O': 1}
assert from_molecules_to_atoms("Mg(OH)2") == {'Mg': 1, 'O': 2, 'H': 2}
