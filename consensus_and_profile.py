#see counting point mutation before
#this is to count a profile sequence in a sample of DNAs
with open("rosalind_cons.txt", "r") as file:
    lines = file.read().strip().split("\n")

sequences = []
seq = ""

for line in lines:
    if line.startswith(">"):
        if seq:
            sequences.append(seq)
            seq = ""
    else:
        seq += line.strip()
if seq:
    sequences.append(seq)

length = len(sequences[0]) #armazena o tamanho da sequências, pegando o tamanho da primeira e assumindo que todas têm o mesmo tamanho

#"inicia" todas as sequências com '0' para cada posição
profile = {
    "A":[0] * length,
    "T":[0] * length,
    "C":[0] * length,
    "G":[0] * length
}

for seq in sequences:
    for i, base in enumerate(seq):
        if base in profile:
            profile[base][i] += 1

#para a sequência consenso
consensus = []
for i in range(length):
    counts = {base: profile[base][i] for base in "ACGT"}
    max_base = max(counts, key=counts.get)
    consensus.append(max_base)

consensus_seq = "".join(consensus)

print(consensus_seq)
for base in "ACGT":                                         #AQUI PRECISA ESTAR NA MESMA ORDEM DO EXEMPLO DO EXERCICIO 
    print(f"{base}: {' '.join(map(str, profile[base]))}")