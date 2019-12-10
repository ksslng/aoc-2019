import numpy as np
import sympy
from fractions import Fraction
import itertools as it

with open('day10', 'r') as f:
    t = f.read()[:-1]

t = t.splitlines()
#m = np.array(t)
m = np.array([[x for x in l] for l in t])
print(m.shape)
print(m)

mmax = 0
coords = (0,0)
frac = [Fraction(x,y) for x in range(1, m.shape[0], 1) for y in range(1,m.shape[1],1)]
frac.sort()
print(frac)
mask = np.ma.array(m)
for x,y in np.ndindex(m.shape):
    c = 0
    #saved_ratio = [(Fraction(0, 0), 0)]
    if m[x,y] == '#':
        '''
        for cx,cy in np.ndindex(m.shape):
            test = (Fraction(cx - x,cy - y), sum(1 for i in [cx - x, cy - y] if i < 0))
            if test in saved_ratio:
                print(f"x,y: ({x}, {y}) cx,cy: {(cx,cy)}")
                saved_ratio.append(test)
                c += 1

        '''
        mask.mask = np.ma.nomask
        mask[x,y] = np.ma.masked
        #print(mask)
        #print(f"test ({x}, {y})")
        for sx in it.chain.from_iterable([range(m.shape[0]), range(-1, -m.shape[0], -1)]):
            for sy in it.chain.from_iterable([range(m.shape[1]), range(-1, -m.shape[1], -1)]):
                '''
                if not sympy.isprime(abs(sy)) and abs(sy) not in [0, 1]:
                    continue
                if sx == 0 and abs(sy) > 1 or sy == 0 and abs(sx) > 1 or (abs(sy) == abs(sx) and abs(sx) != 1):
                    continue
                '''
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
                        marked = True
                    mask[x + i * sx, y + i * sy] = np.ma.masked
                    i += 1
                    
        #print(f"x,y: ({x}, {y}) count: {c}")
        #print(mask)
        
    if mmax < c:
        mmax = c
        coords = (x,y)
        print(f"x,y: {coords} count: {mmax}")

print(f"x,y: {coords} count: {mmax}")