collection = {}
label = None
seq_lines = []

with open("teste.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line.startswith(">"):
            if label:
                collection[label] = ''.join(seq_lines)
            label = line
            seq_lines = []
        else:
            seq_lines.append(line)
    if label:
        collection[label] = ''.join(seq_lines)

for label, seq in collection.items():
    print(label)
    print(seq)