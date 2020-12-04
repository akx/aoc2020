from string import hexdigits

from d04lib import read_d04, good_ecl, required_fields


def validate_hgt(x):
    if x.endswith("in"):
        return 59 <= int(x[:-2]) <= 76
    if x.endswith("cm"):
        return 150 <= int(x[:-2]) <= 193
    return False


validators = {
    "byr": lambda x: 1920 <= int(x) <= 2002,
    "iyr": lambda x: 2010 <= int(x) <= 2020,
    "eyr": lambda x: 2020 <= int(x) <= 2030,
    "hgt": validate_hgt,
    "hcl": lambda x: len(x) == 7 and x[0] == "#" and all(c in hexdigits for c in x[1:]),
    "ecl": lambda x: x in good_ecl,
    "pid": lambda x: len(x) == 9 and x.isdigit(),
    "cid": lambda x: True,
}

passports = read_d04()
passports = [
    p
    for p in passports
    if set(p.keys()) >= required_fields
    and all(validators[key](value) for (key, value) in p.items())
]
print(len(passports))
