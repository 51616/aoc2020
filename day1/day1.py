import sys

def part_one(inp):
    i = 0
    j = len(inp)-1
    while True:
        if inp[i]+inp[j]>target:
            j -= 1
        elif inp[i]+inp[j]<target:
            i += 1
        else:
            return inp[i]*inp[j]

def part_two(inp):
    s = set(inp)
    i = 0
    j = len(inp)-1
    while True:
        if inp[i]+inp[j]>=target:
            j -= 1
        elif inp[i]+inp[j]<target:
            res = target-inp[i]-inp[j]
            if res in s:
                k = inp.index(res)
                return inp[i]*inp[j]*inp[k]
            i += 1
        
if __name__=='__main__':
    target = 2020
    inp = sys.stdin.read()
    inp = [int(i) for i in inp.split()]
    inp.sort()
    out_1 = part_one(inp)
    out_2 = part_two(inp)
    print(f'Part one: {out_1}')
    print(f'Part two: {out_2}')