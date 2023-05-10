p = 3
q = 5
n = p * q
e = 65535

for m in range (n):
    if pow(m, e, n) == 10:
        print("m =", m)
        break