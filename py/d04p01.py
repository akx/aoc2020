from d04lib import read_d04, required_fields

passports = read_d04()
print(len([p for p in passports if set(p.keys()) >= required_fields]))
