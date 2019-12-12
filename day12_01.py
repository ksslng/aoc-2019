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

moons_pos = []
moons_vel = []
for l in t:
    #print(l)
    l = [int(s[2:]) for s in l[1:-2].replace(' ', '').split(',')]
    moons_pos.append(l)
    moons_vel.append([0,0,0])

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
    for i in range(len(moons_pos)):
        for j in range(len(moons_pos)):
            if i == j:
                continue
            moons_vel[i] = [*map(operator.add, moons_vel[i],
                        [*map(lambda a, b: vel_change(a,b), moons_pos[i], moons_pos[j])])]


def update_position():
    global moons_vel, moons_pos
    for i in range(len(moons_pos)):
        moons_pos[i] = [*map(operator.add, moons_pos[i], moons_vel[i])]

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
while True:
    #print(f"step {step}\n{moons_pos}\n{moons_vel}")
    a = hash(tuple(map(tuple,moons_pos)))
    if a in h:
        print(f"found: {step}")
    h.add(a)
    update_velocity()
    update_position()
    step += 1
    if step %100000 == 0:
        print(f"{step} {time.time() - ti}")
        ti = time.time()

print(calculate_total())