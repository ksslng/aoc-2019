f = open("day05", "r").readline()

t = f.split(",")

para_count_arr = [1, 3, 3, 1, 1, 2, 2, 3, 3]

code = list(map(int, t))
code.extend([0] * 50)
print(code)

pos = 0
while code[pos] != 99:
    p_mode = list(map(int, str(int(code[pos] / 100))))
    p_mode.reverse()
    p_mode.extend([0,0,0])
    opcode = code[pos] % 100
    para_count = para_count_arr[opcode]
    para = []
    print(f"pos:{pos}\tcode[pos]:{code[pos]}")
    for i in range(0, para_count):
        if p_mode[i] == 0:
            para.append(code[code[pos + 1 + i]])
        else:
            para.append(code[pos + 1 + i])
    if opcode == 1:
        code[code[pos + 3]] = para[0] + para[1]
    elif opcode == 2:
        code[code[pos + 3]] = para[0] * para[1]
    elif opcode == 3:
        code[code[pos + 1]] = int(input("Input:"))
    elif opcode == 4:
        print(para[0])
    elif opcode == 5:
        pos = para[1] - para_count - 1 if para[0] != 0 else pos
    elif opcode == 6:
        pos = para[1] - para_count - 1 if para[0] == 0 else pos
    elif opcode == 7:
        code[code[pos + 3]] = 1 if para[0] < para[1] else 0
    elif opcode == 8:
        code[code[pos + 3]] = 1 if para[0] == para[1] else 0
    pos += para_count + 1

print(code)