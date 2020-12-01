with open("d01-input.txt", "r") as f:
	entries = [int(ent.strip()) for ent in f]
	for i, a in enumerate(entries):
		for b in entries[:i]:
			if a + b == 2020:
				print(a * b)
				break