import numpy as np
import sympy
from fractions import Fraction
import itertools as it

with open('day10', 'r') as f:
    t = f.read()

t = t.splitlines()
#m = np.array(t)
m = np.array([[x for x in l] for l in t])
print(m.shape)
print(m)

frac = [Fraction(x,y) for x in range(1, 30, 1) for y in range(1,30,1)]
frac.sort()
print(frac)
frac = list(set(frac))
frac.sort()
print(frac)

mmax = 0
x = 17
y = 13
c = 1
mask = np.ma.array(m)
mask[x,y] = np.ma.masked

def go_dir(x, y, sx, sy):
    global c, mask, m
    i = 1
    marked = False
    while 0 <= x + i * sx < m.shape[0] and 0 <= y + i * sy < m.shape[1]:
        #if mask[x + i * sx, y + i * sy] in ['.', '#']:
        #    break
        #print(f"\t\tcheck ({x + i * sx}, {y + i * sy}) {m[x + i * sx, y + i * sy]}")
        if mask[x + i * sx, y + i * sy] == '#' and not marked:
            print(f"{c}:\t{(x + i * sx, y + i * sy)}")
            c += 1
            mask[x + i * sx, y + i * sy] = '.'
            marked = True
        #mask[x + i * sx, y + i * sy] = np.ma.masked
        i += 1

while np.count_nonzero(mask == '#') > 0:
    go_dir(x, y, -1, 0)
    for d in frac:
        #print(d)
        go_dir(x, y, -d.denominator, d.numerator)
    go_dir(x, y, 0, 1)
    for d in frac:
        go_dir(x, y, d.numerator, d.denominator)
    go_dir(x, y, 1, 0)
    for d in frac:
        go_dir(x, y, d.denominator, -d.numerator)
    go_dir(x, y, 0, -1)
    for d in frac:
        go_dir(x, y, -d.numerator, -d.denominator)
    '''
    for ort in [((0, m.shape[0], 1), (-m.shape[0], 0, -1)), (1, 1), (1, -1), (-1, -1)]:
    #saved_ratio = [(Fraction(0, 0), 0)]

        #print(mask)
        #print(f"test ({x}, {y})")
        for sx in range(0, m.shape[0] * ort[0], ort[0]):
            for sy in range(0, m.shape[1] * ort[1], ort[1]):
                
                if not sympy.isprime(abs(sy)) and abs(sy) not in [0, 1]:
                    continue
                if sx == 0 and abs(sy) > 1 or sy == 0 and abs(sx) > 1 or (abs(sy) == abs(sx) and abs(sx) != 1):
                    continue
                
                #print(f"\tmade it ({sx}, {sy})")
                i = 1
                if sx == 0 and sy == 0:
                    continue
                #print(f"\tstart to check ({x + i * sx}, {y + i * sy})")
                marked = False
                while 0 <= x + i * sx < m.shape[0] and 0 <= y + i * sy < m.shape[1]:
                    #if mask[x + i * sx, y + i * sy] in ['.', '#']:
                    #    break
                    #print(f"\t\tcheck ({x + i * sx}, {y + i * sy}) {m[x + i * sx, y + i * sy]}")
                    if mask[x + i * sx, y + i * sy] == '#' and not marked:

                        
                        #print(f"\t\tx,y: ({x}, {y}) i: {i} sx,sy: ({sx}, {sy}) \tcount: ({x + i * sx}, {y + i * sy})")
                        c += 1
                        break
                    mask[x + i * sx, y + i * sy] = np.ma.masked
                    i += 1
                    
        #print(f"x,y: ({x}, {y}) count: {c}")
        #print(mask)
        
    if mmax < c:
        mmax = c
        coords = (x,y)
        print(f"x,y: {coords} count: {mmax}")
    '''
    #break

#print(f"x,y: {coords} count: {mmax}")