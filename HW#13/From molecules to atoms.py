import re


def from_molecules_to_atoms(formula):
    dict2 = {}

    if "[" in formula:
        match = re.search(r"\(([^\)]+)\)(\d*)", formula)
        dict1 = {}

        if match:
            for element, number in re.findall(r"([A-Z][a-z]?)(\d*)", match.group(1)):
                multiplier = int(match.group(2)) if match.group(2) else 1
                dict1[element] = (int(number) if number else 1) * multiplier

            str1 = "".join(f"{key}{value}" for key, value in dict1.items())
            newformula = re.sub(r"\(([^\)]+)\)(\d*)", str1, formula)
        else:
            newformula = formula

        match2 = re.search(r"\[([^\]]+)\](\d*)", newformula)

        if match2:
            for element, number in re.findall(r"([A-Z][a-z]?)(\d*)", match2.group(1)):
                count = int(number) if number else 1
                multiplier = int(match2.group(2)) if match2.group(2) else 1
                dict2[element] = dict2.get(element, 0) + count * multiplier

            newformula2 = re.sub(r"\[([^\]]+)\](\d*)", '', newformula)
        else:
            newformula2 = newformula

    elif "(" in formula:
        match = re.search(r"\(([^\)]+)\)(\d*)", formula)
        dict1 = {}

        if match:
            for element, number in re.findall(r"([A-Z][a-z]?)(\d*)", match.group(1)):
                multiplier = int(match.group(2)) if match.group(2) else 1
                dict1[element] = (int(number) if number else 1) * multiplier

            str1 = "".join(f"{key}{value}" for key, value in dict1.items())
            newformula2 = re.sub(r"\(([^\)]+)\)(\d*)", str1, formula)
        else:
            newformula2 = formula  #

    else:
        newformula2 = formula

    for element, number in re.findall(r"([A-Z][a-z]?)(\d*)", newformula2):
        count = int(number) if number else 1
        dict2[element] = dict2.get(element, 0) + count

    return dict2


print(from_molecules_to_atoms("K4[ON(SO3)2]2"))
print(from_molecules_to_atoms("H2O"))
print(from_molecules_to_atoms("Mg(OH)2"))
assert from_molecules_to_atoms("K4[ON(SO3)2]2") == {'O': 14, 'N': 2, 'S': 4, 'K': 4}
assert from_molecules_to_atoms("H2O") == {'H': 2, 'O': 1}
assert from_molecules_to_atoms("Mg(OH)2") == {'Mg': 1, 'O': 2, 'H': 2}
