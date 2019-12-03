import numpy as np

def get_dir(dir):
    if dir == "R":
        return np.array((1, 0))
    if dir == "L":
        return np.array((-1, 0))
    if dir == "D":
        return np.array((0, 1))
    if dir == "U":
        return np.array((0, -1))


lowest = 999999
m = dict()
with open("day03", "r") as f:
    t = f.read()

#t = "R8,U5,L5,D3\nU7,R6,D4,L4"
t = [l.split(',') for l in t.splitlines()]
print(t)
t = [[(get_dir(x[:1]), int(x[1:])) for x in run] for run in t]
print(t)
pos = np.array((0, 0))

i = 1
for r in t[0]:
    for s in range(0, r[1]):
        pos += r[0]
        #print(tuple(pos))
        m[tuple(pos)] = i
        i += 1
i = 1
pos = np.array((0, 0))
for r in t[1]:
    for s in range(0, r[1]):
        pos += r[0]
        #print(tuple(pos))
        if tuple(pos) in m:
            c = m[tuple(pos)] + i
            print(c)
            if c < lowest:
                lowest = c
        i +=1
            

print(lowest)

