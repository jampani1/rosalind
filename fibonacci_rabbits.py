#A key observation is that the number of offspring in any month is equal to the number of rabbits that were alive two months prior.
#Leonardo of Pisa aka Fibonacci counts rabbits etc
#Although the sequence bears Fibonacci's name, it was known to Indian mathematicians over two millennia ago.
#Fib   F(n) = F(n-1) + k * F(n-2)
#dynamic programming

#rabbits = initial counting (two first mounths)
#n (mounths)

rabbits = [1, 1]
n = 0;

with open ("rosalind_fib.txt", "r") as file:
    #grabbing n and k
    nk = file.read().strip().split(' ')
    n = int(nk[0])
    k = int(nk[1])
    for i in range(2, n): #começa no mês 3 (índice 2)
        next_value = rabbits[i - 1] + k * rabbits[i - 2]
        rabbits.append(next_value)
    print(rabbits[-1]) #show last number only