import sys
import numpy as np

def part_one(inp):
    inp = [int(x) for x in inp if len(x)>0]
    for i in range(len(inp)):
        if i <25:
            continue
        val = inp[i]
        s = set(inp[i-25:i])
        for j in range(i-25,i):
            if (val-inp[j]) in s:
                break
            if j==i-1:
                return val

def part_two(inp):
    target = out_1
    inp = [int(x) for x in inp if len(x)>0]
    csum = np.cumsum(inp)
    cpair = np.zeros([len(csum)]*2)
    for i in range(len(csum)):
        for j in range(i):
            cpair[i,j] = csum[i]-csum[j]

    for coord in np.argwhere(cpair==target):
        cont_list = inp[coord[1]+1:coord[0]+1]
        return min(cont_list)+max(cont_list)


if __name__=='__main__':
    inp = sys.stdin.read()

    out_1 = part_one(inp.split('\n'))
    print(f'Part one: {out_1}')

    out_2 = part_two(inp.split('\n'))
    print(f'Part two: {out_2}')