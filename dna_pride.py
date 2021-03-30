num_lin = int(input())

for i in range(num_lin):
	base_pair = ""
	num_char = int(input())
	dna_seq = input()
	for j in range(num_char):
		if dna_seq[j] == "U":
			base_pair = "Error RNA nucleobases found!"
			break
		elif dna_seq[j] == "A":
			base_pair += "T"
		elif dna_seq[j] == "T":
			base_pair += "A"
		elif dna_seq[j] == "C":
			base_pair += "G"
		elif dna_seq[j] == "G":
			base_pair += "C"
	print(base_pair)