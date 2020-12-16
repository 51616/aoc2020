import sys
import numpy as np

def part_one(inp):
    inp = [int(x) for x in inp if len(x)>0]
    inp.sort()
    out = 0
    c1 = 0
    c3 = 1
    for i in range(len(inp)):
        if i==0:
            prev = 0
        else:
            prev = inp[i-1]
        dif = inp[i]-prev
        if dif==1:
            c1 += 1
        if dif==3:
            c3 += 1
    out = c1*c3
    return out

def part_two(inp):
    inp = [0] + [int(x) for x in inp if len(x)>0]
    inp.sort()
    tab = np.zeros(len(inp))
    tab[-1] = 1

    def parents(i):
        parents = []
        for j in range(1,4):
            if (i+j<len(inp)) and (inp[i+j]-inp[i]<=3):
                parents.append(tab[i+j])
        tab[i] = sum(parents)
        return tab[i]

    for i in range(len(inp)-2,-1,-1):
        parents(i)

    return tab[0]


if __name__=='__main__':
    inp = sys.stdin.read()

    out_1 = part_one(inp.split('\n'))
    print(f'Part one: {out_1}')

    out_2 = part_two(inp.split('\n'))
    print(f'Part two: {out_2}')