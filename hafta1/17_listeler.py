a = [1, 2, 3]
b = [True, 0.5, 7894561312, None, [1, "ad", 8.5]]

print(a)
print(b)
print(b[0])
print(b[4][1])

tr = "Türkiye"
print(tr[1:4])

b[4][1] = [6, 99, 6.5, "asdasd"]
print(b[4][1])
print(b[4][1][3])
