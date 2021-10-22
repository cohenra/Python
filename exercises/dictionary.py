thisdict = {
    "naftali": "bennet",
    "bibi": "netanyahu",
    "yair": "lapid",
}
x = {}
for key in thisdict.values():

    print(key)
for key, value in thisdict.items():
    x[value] = key
    print(x)