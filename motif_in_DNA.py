#list comprehension ex

import re

with open ("rosalind_subs.txt", "r") as file:
    seq = file.read().strip().split("\n")
    seq_DNA = seq[0]
    DNA_motif = seq[1]

motif = re.finditer(f'(?={DNA_motif})', seq_DNA)

positions = [m.start() + 1 for m in motif] #+1 para posição capturar certo (considera que indice inicia em 0, portanto tem que adicionar 1)
print(*positions) #gera indices
