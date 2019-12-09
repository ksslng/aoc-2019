import numpy as np
import sys
#img = np.array(25,6,1)

with open("day08", "r") as f:
    t = f.read()[:-1]
#t = '0222112222120000'

#l = [[0 for i in range(25)] for x in range(6)]
inp = list(map(int, t))
#for i in range(25 * 6):
#    l[int(i/25)][i%25] = inp[i]

#print(l)

img = np.array(list(map(int, t)))
print(len(img))
n_layers = int(len(img) / 25 / 6)
print(n_layers)
img = np.transpose(img.reshape(25,6,-1, order='F'),axes=(1,0,2))
print(img[:,:,0])
mi = 25 * 6
min_i = 0
for i in range(0, n_layers):
    c = np.count_nonzero(img[:,:,i]==0)
    if c < mi:
        mi = c
        min_i = i
        print(f"{i}: {c}")

print(min_i)
print(np.count_nonzero(img[:,:,min_i]==1))
print(np.count_nonzero(img[:,:,min_i]==2))
res = np.count_nonzero(img[:,:,min_i]==1) * np.count_nonzero(img[:,:,min_i]==2) 
print(img[:,:,min_i])
print(res)

layer = 1
res = img[:,:,0]
while np.count_nonzero(res==2) != 0:
    #print(res)
    res = np.where(res != 2, res, img[:,:, layer])
    layer += 1
print(res)
np.savetxt(sys.stdout, res, delimiter='', newline='',fmt="%i")
#print(''.join(map(int,res)))