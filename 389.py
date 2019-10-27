a = ["a", "b", "c", "d"]
b = ["a", "b", "c", "d", "e"]

c = a.extend(b)

for d in a:
    if (d.count < 2):
        print(d)