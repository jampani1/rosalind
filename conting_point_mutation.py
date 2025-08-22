#evoluiton as a sequence of mistakes!!!
#Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t) , is the number of corresponding symbols that differ in s and t
#HMM distance - search ab

with open("rosalind_hamm.txt", "r") as file:
    seq = file.read().strip().split("\n")
    equals = 0
    for i in range(len(seq[0])):
        if seq[0][i] == seq[1][i]:
            equals += 1

print(len(seq[0]) - equals)