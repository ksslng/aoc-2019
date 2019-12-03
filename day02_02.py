f = open("day02", "r").readline()

t = f.split(",")

code2 = list(map(int, t))

for i in range(0,99):
    for j in range(0,99):
        code = list(code2)
        code[1] = i
        code[2] = j
        pos = 0
        while code[pos] != 99:
            a = code[code[pos + 1]]
            b = code[code[pos + 2]]
            code[code[pos + 3]] = a + b if code[pos] == 1 else a * b
            pos += 4

        if code[0] == 19690720:
            print(i, j)