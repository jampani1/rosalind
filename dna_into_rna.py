#Transcribing DNA into RNA - 2nd ex.
with open("rosalind_rna.txt", "r") as file:
    dna = file.read().strip()
    rna = dna.replace("T", "U")
print(rna)