import sys
from collections import defaultdict

target = 'shiny gold bag'

def part_one(inp):
    d = defaultdict(list)
    for l in inp:
        if len(l)==0:
            continue
        s = l.split('contain')
        # print(s)
        big, small = s[0], s[1]
        big = big.strip()[:-1]
        for b in small.split(','):
            b = b.strip(' s.')
            num = b[0]
            name = b[2:]
            if not num in '0123456789':
                pass
            # print(f'Name: {name}, Num: {num}')
            d[name].append(big)
    parents = d[target]
    
    for bag in parents:
        p = d[bag]
        parents.extend(p)
    out = len(set(parents))

    return out

def part_two(inp):
    d = defaultdict(dict)
    for l in inp:
        if len(l)==0:
            continue
        s = l.split('contain')
        # print(s)
        big, small = s[0], s[1]
        big = big.strip()[:-1]
        for b in small.split(','):
            b = b.strip(' s.')
            num = b[0]
            name = b[2:]
            if not num in '0123456789':
                continue
            # print(f'Name: {name}, Num: {num}')
            d[big][name] = int(num)

    def count_child(name):
        if len(d[name])==0:
            return 0
        c = 0
        for bag, num in d[name].items():
            c += num
            c += num * count_child(bag)
        return c
    out = count_child(target)
    return out

if __name__=='__main__':
    inp = sys.stdin.read()  

    out_1 = part_one(inp.split('\n'))
    print(f'Part one: {out_1}')

    out_2 = part_two(inp.split('\n'))
    print(f'Part two: {out_2}')