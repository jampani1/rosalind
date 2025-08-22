#Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that all rabbits die out after a fixed number of months. For a depiction of a rabbit tree in which rabbits live for three months (meaning that they reproduce only twice before dying).
#positive integers n <= 100 and m <= 20
#The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months

#Ex input: 6 3 (6 m; living for 3 m)
#return 4

#coelhos com 1 mês de vida não se reproduzem (0)
#a partir do 1 mes eles se reproduzem todo mês até morrerem (+1)
#eles morrem após x meses (-1)

#lista onde cada item representa a idade dos coelhos
#coelhos = [n0, n1, n2, ..., nX-1]
#onde coelhos[0] é a quantidade de coelhos recem nascidos (0 meses)
# coelhos[1] é a quantidade de coelhos com 1 mes de vida
# coelhos[X-1] é a quantidade de coelhos com X-1 meses (no próximo mês, morrerão)

coelhos = [0]

with open ("rosalind_fibd.txt", "r") as file:
    meses_vida = file.read().strip().split(' ')
    meses = int(meses_vida[0]) #number of mounths 
    vida = int(meses_vida[1]) #life duration

#sum(coelhos[1:]) soma todos os coelhos com 1 mês ou mais (todos com 1+ reproduzem)
#[novos] + coelhos[:-1] considera os que envelhecem, sendo que os mais velhos morrem

    coelhos = [1] + [0] * (vida-1)
    for _ in range (1, meses):
        novos = sum(coelhos[1:])
        coelhos = [novos] + coelhos[:-1]
    print(sum(coelhos))

