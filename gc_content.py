def gc_content(seq):
    g = seq.count('G')
    c = seq.count('C')
    return ((g + c) / len(seq)) * 100

with open ("rosalind_gc.txt", "r") as file:
    text = file.read().strip().split("\n")

dados = {}
label = ''
sequencia = ''

for linha in text:
    if linha.startswith('>'):
        if label:
            dados[label] = sequencia
        label = linha[1:] #desconsidera o # no label
        sequencia = ''
    else:
        sequencia += linha.strip()

if label:
    dados[label] = sequencia

maior_gc = 0
label_maior_gc = ''

for label, seq in dados.items():
    gc = gc_content(seq)
    if gc > maior_gc:
        maior_gc = gc
        label_maior_gc = label

print(label_maior_gc)
print(f"{maior_gc:.6f}")

