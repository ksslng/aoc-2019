orbs = dict()
with open("day06_test", "r") as f:
    for l in f.read().splitlines():
        c, o = tuple(l.split(')'))
        orbs[o] = c

def step_orbs(o1, o2):
    l1 = []
    l2 = []
    while o1 in orbs:
        l1 += [o1]
        o1 = orbs[o1]
    while o2 not in l1:
        l2 += [o2]
        o2 = orbs[o2]
    l1 = l1[:l1.index(o2)]
    l2.reverse()
    print(len(l1) + len(l2), l1,l2)


step_orbs("YOU", "SAN")
