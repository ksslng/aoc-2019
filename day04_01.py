c = 0
for i in range(246515, 739105):
    k = list(map(int, str(i)))
    same = 0
    for j in range(0,5):
        if k[j] == k[j + 1] and k.count(k[j]) == 2:
            same = 1
        elif k[j] > k[j + 1]:
            break
    else:
        if same == 1 :
            print(i)
            c += 1

print(c)