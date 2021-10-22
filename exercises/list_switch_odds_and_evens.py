x = int(input("insert a len of list:"))
list_num = []
for i in range(x):
    list_num.append(int(input("insert a number:")))
print(list_num)
y = 0
old = list_num[0]
for num in list_num:
    if num % 2 == 0 and old % 2 != 0 or num % 2 != 0 and old % 2 == 0:
        list_num[y] = old
        list_num[y-1] = num
    old = list_num[y]
    y += 1
print(list_num)
