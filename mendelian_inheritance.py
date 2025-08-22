#remember 
#AA x AA - 100% AA
#AA x Aa - 50% AA 50% Aa 
#Aa x Aa - 25% AA 50% Aa 25% aa
#aa x aa - 100% aa

#dict com probabilidades de ser o fenótipo dominante
dominant_probs = {
    ("AA", "AA"): 1.0,
    ("AA", "Aa"): 1.0,
    ("AA", "aa"): 1.0,
    ("Aa", "Aa"): 0.75,
    ("Aa", "aa"): 0.5,
    ("aa", "aa"): 0.0,
}

with open ("rosalind_iprb.txt", "r") as file:
    total = 0
    content = file.read().strip().split(" ")
    k = int(content[0]) #homozigoto AA
    m = int(content[1]) #heterozigoto Aa
    n = int(content[2]) #homozigoto recessivo aa
    genotypes = [("AA", k), ("Aa", m), ("aa", n)]
    total = k + m + n
    probability = 0.0   #probabilidade total iniciada em 0
    for i in range(len(genotypes)):
        for j in range(i, len(genotypes)): #evita contar pares repetidos, tipo Aa x aa e aa x Aa
            geno1, count1 = genotypes[i]
            geno2, count2 = genotypes[j]
            if i == j:                                                          #calcular % dois genot =
                prob_pair = (count1 / total) * ((count1 - 1) / (total - 1))     #AA primeiro e count1 - 1
            else:                                                               ##calcular % dois %
                prob_pair = 2 * (count1 / total) * (count2 / (total - 1))       ##vezes 2 para 2 ordens
            
            key = (geno1, geno2) if (geno1, geno2) in dominant_probs else (geno2, geno1)
            prob_dom = dominant_probs[key]
            probability += prob_pair * prob_dom
    print(round(probability, 5))




