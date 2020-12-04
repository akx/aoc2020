SEP = chr(30)
with open("../inputs/d04-input.txt") as f:
    data = f.read()
    data = data.replace("\n\n", SEP)
    data = data.replace("\n", " ")
passports = [raw.split() for raw in data.split(SEP)]
passports = [dict(p.split(":", 1) for p in row) for row in passports]

required_fields = {
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
}

print(len([p for p in passports if set(p.keys()) >= required_fields]))
