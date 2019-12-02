f = open("day01", "r")
s = 0
def calc_fuel(x):
    new_x = int(x / 3) - 2
    if new_x <= 0:
        return 0
    return calc_fuel(new_x) + new_x

for x in f.readlines():
    s += calc_fuel(int(x))

print(calc_fuel(1969))

print(s)