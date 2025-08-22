#brief introduction to graph theory
#considera o link entre duas sequências (sufixo > prefixo) os trechos de 3 nucleotideos (O3)

with open("rosalind_grph.txt", "r") as file:
    sequences = {}
    seq_label = None
    seq = []
    for line in file:
        line = line.strip()
        if line.startswith(">"):
            if seq_label:
                sequences[seq_label] = ''.join(seq)
            seq_label = line[1:]
            seq = []
        else:
            seq.append(line)
    if seq_label:
        sequences[seq_label] = ''.join(seq)

for id1, seq1 in sequences.items():
    suffix = seq1[-3:]
    for id2, seq2 in sequences.items():
        if id1 != id2 and seq2.startswith(suffix):
            print(id1, id2)