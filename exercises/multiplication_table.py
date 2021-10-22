"""x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
multiplication = []
sum = 0
for i in (x):
    for z in (y):
        multiplication.append([int(i) * int(z)])
        sum += int(i) * int(z)
    print(multiplication)
    multiplication.clear()
print(sum)
"""
row = 1
while row <= 10:
    col = 1
    while col <= 10:
        print(row * col, end='\t')
        col += 1
    print()
    row += 1