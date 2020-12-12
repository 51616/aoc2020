import sys
import numpy as np

def part_one(inp):
    width = len(inp[0])
    r = 3
    d = 1
    i = j = 0
    out = 0
    while True:
        i += d
        if i >= len(inp):
            break
        j += r
        if inp[i][j%width]=='#':
            out += 1
    return out

def part_two(inp):
    width = len(inp[0])
    R = (1,3,5,7,1)
    D = (1,1,1,1,2)
    out = []
    for (r,d) in zip(R,D):
        i = j = 0
        tree = 0
        while True:
            i += d
            if i >= len(inp):
                break
            j += r
            if inp[i][j%width]=='#':
                tree += 1
        print(tree)
        out.append(tree)
    return np.prod(out)

if __name__=='__main__':
    inp = sys.stdin.read()
    inp = inp.split('\n')[:-1]
    print(inp)
    out_1 = part_one(inp)
    print(f'Part one: {out_1}')

    out_2 = part_two(inp)
    print(f'Part two: {out_2}')