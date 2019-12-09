f = open("day09", "r").readline()
#f = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
#f = "1102,34915192,34915192,7,4,7,99,0"
#f = "104,1125899906842624,99"
t = f.split(",")

para_count_arr = [1, 3, 3, 1, 1, 2, 2, 3, 3, 1]

code = list(map(int, t))
code.extend([0] * 5000)
print(code)

rel_base = 0
pos = 0
while code[pos] != 99:
    p_mode = list(map(int, str(int(code[pos] / 100))))
    p_mode.reverse()
    p_mode.extend([0,0,0])
    opcode = code[pos] % 100
    para_count = para_count_arr[opcode]
    para = []
    #print(f"pos:{pos}\tcode[pos]:{code[pos]}\trel_base:{rel_base}")
    #print(f"\t{[code[pos + i + 1] for i in range(0, para_count)]}")
    for i in range(0, para_count):
        if p_mode[i] == 0:
            para.append(code[code[pos + 1 + i]])
        elif p_mode[i] == 2:
            para.append(code[rel_base + code[pos + 1 + i]])
        else:
            para.append(code[pos + 1 + i])
    
    #print(f"\t{[para[i] for i in range(0, para_count)]}") 
    if opcode == 1:
        if p_mode[2] == 2:
            code[rel_base + code[pos + 3]] = para[0] + para[1]
            #print(f"\tsave2 at {rel_base + code[pos + 1]}: {para[0] * para[1]}")
        else:
            code[code[pos + 3]] = para[0] + para[1]
            #print(f"\tsave at {code[pos + 3]}: {para[0] + para[1]}")
    elif opcode == 2:
        if p_mode[2] == 2:
            code[rel_base + code[pos + 3]] = para[0] * para[1] 
            #print(f"\tsave2 at {rel_base + code[pos + 1]}: {para[0] * para[1]}")
        else:
            code[code[pos + 3]] = para[0] * para[1]
            #print(f"\tsave at {code[pos + 3]}: {para[0] * para[1]}")
    elif opcode == 3:
        if p_mode[0] == 2:
            code[rel_base + code[pos + 1]] = int(input("Input:")) 
            #print(f"\tsave2 at {rel_base + code[pos + 1]}: {code[rel_base + code[pos + 1]]}")
        else:
            code[code[pos + 1]] = int(input("Input:"))
            print(f"\tsave at {code[pos + 1]}: {code[code[pos + 1]]}")
    elif opcode == 4:
        print(para[0])
    elif opcode == 5:
        pos = para[1] - para_count - 1 if para[0] != 0 else pos
    elif opcode == 6:
        pos = para[1] - para_count - 1 if para[0] == 0 else pos
    elif opcode == 7:
        if p_mode[2] == 2:
            code[rel_base + code[pos + 3]] = 1 if para[0] < para[1] else 0
        else:
            code[code[pos + 3]] = 1 if para[0] < para[1] else 0
    elif opcode == 8:
        if p_mode[2] == 2:
            code[rel_base + code[pos + 3]] = 1 if para[0] == para[1] else 0
        else:
            code[code[pos + 3]] = 1 if para[0] == para[1] else 0
    elif opcode == 9:
        rel_base += para[0]
    pos += para_count + 1

#print(code)