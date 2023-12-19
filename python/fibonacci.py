szam_elozo0 = 0
szam_elozo1 = 1

for i in range(2, 51):
    fibonacci = szam_elozo0 + szam_elozo1
    szam_elozo0 = szam_elozo1
    szam_elozo1 = fibonacci

fibonacci_str = str(fibonacci)
erdmeny = int(fibonacci_str[-1]) - int(fibonacci_str [0])
print(erdmeny)