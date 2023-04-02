D = { "0":0, "1":1, "2":4, "3":9, "4":16,
      "5":25, "6":36, "7":49, "8":64, "9":81}   

Lookup = [89, 145, 42, 20, 4, 16, 37, 58, 89]

def IsHappy(n):
    while(True):
        n = sum(D[s] for s in str(n))
        if n == 1:
            return True
        # Check for the beginning of the infinite cycle
        if n == 4:
            return False
    return False

s = 0
for i in range(1, 10000000):
    if IsHappy(i):
        s += 1

# Answer = sum(1 for i in range(1, 10000000) if IsHappy(i))

print(s)
print(10000000-1-s)