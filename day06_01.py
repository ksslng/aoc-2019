orbs = dict()
with open("day06", "r") as f:
    for l in f.read().splitlines():
        c, o = tuple(l.split(')'))
        orbs[o] = c

def count_orbs(o):
    if o in orbs:
        return count_orbs(orbs[o]) + 1
    return 0

print(sum(map(count_orbs, orbs.keys())))