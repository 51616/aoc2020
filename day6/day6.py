import sys
from collections import defaultdict

def part_one(inp):
    out = 0
    s = set()
    for l in inp:
        if len(l)==0:
            out += len(s)
            s = set()
            continue
        for c in l:
            s.add(c)
    return out

def part_two(inp):
    out = 0
    d = defaultdict(int)
    c = 0
    for l in inp:
        if len(l)==0:
            for k,v in d.items():
                if v==c:
                    out += 1
            d = defaultdict(int)
            c = 0
            continue
        c += 1
        for ch in l:
            d[ch] += 1
    return out

if __name__=='__main__':
    inp = sys.stdin.read()
    print(inp)    

    out_1 = part_one(inp.split('\n'))
    print(f'Part one: {out_1}')

    out_2 = part_two(inp.split('\n'))
    print(f'Part two: {out_2}')