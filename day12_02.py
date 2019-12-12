from dataclasses import dataclass
import operator
import numpy as np
import time

@dataclass
class Point:
    x: int
    y: int
    z: int

with open('day12', 'r') as f:
    t = f.readlines()
    print(t)

moons_pos = np.zeros((4, 3), dtype=np.int64)
moons_vel = np.zeros((4, 3), dtype=np.int64)
print(moons_pos)
for i in range(4):
    #print(l)
    l = [int(s[2:]) for s in t[i][1:-2].replace(' ', '').split(',')]
    moons_pos[i] = l
    moons_vel[i] = [0,0,0]

#moons_pos = np.array(moons_pos)
#moons_vel = np.array(moons_vel)

def vel_change(a, b):
    if a > b:
        return -1
    if a < b:
        return 1
    return 0

def update_velocity():
    global moons_vel, moons_pos
    r = np.array([3, 0, 1, 2])
    moons_pos[r]
    moons_vel = np.add(moons_vel, np.sign(np.subtract(moons_pos, moons_pos)))
    moons_pos[r]
    moons_vel = np.add(moons_vel, np.sign(np.subtract(moons_pos, moons_pos)))
    moons_pos[r]
    moons_vel = np.add(moons_vel, np.sign(np.subtract(moons_pos, moons_pos)))
    moons_pos[r]


def update_position():
    global moons_vel, moons_pos
    moons_pos = np.add(moons_pos, moons_vel)
    #for i in range(len(moons_pos)):
    #    moons_pos[i] = [*map(operator.add, moons_pos[i], moons_vel[i])]

def calculate_total():
    global moons_vel, moons_pos
    total = 0
    for i in range(len(moons_pos)):
        print(moons_vel[i])
        total += sum(map(abs, moons_pos[i])) * sum(map(abs, moons_vel[i]))
    return total



print(moons_pos)
h = set()
step = 0
ti = time.time()

res = []
for i in range(3):
    p = moons_pos.copy()
    v = moons_vel.copy()
    v += np.sign(p[:,np.newaxis]-p).sum(0)
    p += v
    step = 1
    while not np.array_equal(v[:,i], [0,0,0,0]):
        v += np.sign(p[:,np.newaxis]-p).sum(0)
        p += v
        step += 1
    print(v)
    res.append(2*step)
print(res)
print(np.lcm.reduce(res))

while step < 0:
    #print(f"step {step}\n{moons_pos}\n{moons_vel}")
    #a = moons_pos.dumps()
    #if a in h:
    #    print(f"found: {step}")
    #h.add(a)
    moons_vel += np.sign(moons_pos[:,np.newaxis]-moons_pos).sum(0)
    #print(f"a:{moons_pos[:,np.newaxis]}\nb: {moons_pos}\nc: {moons_pos[:,np.newaxis]-moons_pos}")
    moons_pos += moons_vel
    step += 1
    if step %100000 == 0:
        print(f"{step} {time.time() - ti}")
        ti = time.time()



print(calculate_total())