import math
def binomial_pmf(n, k, p):
    combination = math.comb(n, k)
    pmf = combination * (p ** k) * ((1 - p) ** (n - k))
    return pmf
num = 0
for i in range(0,13):
    num = num +binomial_pmf(30,i,0.3)
print(1-num)