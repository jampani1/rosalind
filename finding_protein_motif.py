#[isso ou aquilo]
#{qualquer coisa menos isso}
#utilização de regex para essa estruturação
#para qualquer aminoácido que não seja um em específico > {X} em regex [^X]
#para um aminoácido dentro de uma "gama" de opções é da mesma forma > [XY]
#no regex então: N[^P][ST][^P]

import re
import requests
pattern = r"(?=(N[^P][ST][^P]))"
#adição de ?=(), ou seja, lookahead, para checar cada posição da sequência sem "pular" após achar um match

with open("rosalind_mprt.txt", "r") as file:
    ids = file.read().strip().split("\n")

for pid in ids:
    acession = pid.split("_")[0] #para pegar sempre só o ID válido, antes de _caso exista
    url = f"https://www.uniprot.org/uniprot/{acession}.fasta"
    response = requests.get(url)

    #response.text contém o cabeçalho + sequência
    #.split("\n") separa em cabeçalho e sequência
    #if line and not line.startswith(">") separa as linhas que contém a sequência (evita cabeçalho e vazias)
    #"".join() junta as linhas filtradas em uma única string contínua
    seq = "".join(line.strip() for line in response.text.split("\n") if line and not line.startswith(">"))

    matches = re.finditer(pattern, seq)
    positions = [m.start() + 1 for m in matches]

    if positions:
        print(pid)
        print(" ".join(map(str, positions))) 
#map(str, positions) transforma os números de positions em strings