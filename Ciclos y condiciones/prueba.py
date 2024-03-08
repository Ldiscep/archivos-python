s = ""
for _ in range(1000):
    s += 'a'
    print(id(s))
    print(s)