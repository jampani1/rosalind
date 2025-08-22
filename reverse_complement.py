#3rd ex. ab complementing a strand of DNA
complement = {"A": "T", "T":"A", "C": "G", "G": "C"} #aux para trocar
result = ""

with open ("rosalind_revc.txt","r") as file:
    dna = file.read().strip()
    invertida = dna[::-1] #ler a string de trás para frente
    for base in invertida:
        result += complement[base]

print(result)   