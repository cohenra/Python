digits = "123342352562341234108"
counter = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
for i in digits:
    if i in counter:
        counter[i] += 1
    else:
        print("wrong! insert just digits")
        break
else:
    print(counter)