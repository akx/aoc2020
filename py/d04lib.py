def read_d04():
    SEP = chr(30)
    with open("../inputs/d04-input.txt") as f:
        data = f.read()
        data = data.replace("\n\n", SEP)
        data = data.replace("\n", " ")
    passports = [
        dict(sorted(p.split(":", 1) for p in row))
        for row in (raw.split() for raw in data.split(SEP))
    ]
    return passports


good_ecl = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

required_fields = {
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
}
