with open("d01-input.txt", "r") as f:
	entries = [int(ent.strip()) for ent in f]
	for i, a in enumerate(entries):
		for j, b in enumerate(entries[:i]):
			for c in entries[:(i + j)]:
				if a + b + c == 2020:
					print(a * b * c)
					break