f = open("day02", "r").readline()

t = f.split(",")

code = list(map(int, t))
code[1] = 12
code[2] = 2
pos = 0
while code[pos] != 99:
    a = code[code[pos + 1]]
    b = code[code[pos + 2]]
    code[code[pos + 3]] = a + b if code[pos] == 1 else a * b
    pos += 4

print(code)