f = open("day01", "r")
s = 0
for x in f.readlines():
    s += int(int(x) / 3) - 2

print(s)