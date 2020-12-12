import sys

VAL = {'F':'0', 'B':'1', 'L':'0', 'R':'1'}

def bin_to_dec(x):
    out = 0
    for i in range(len(x)):
        out += 2**i*int(x[-1-i])
    return out

def part_one(inp):
    out = 0
    for l in inp:
        bin = ''.join(list(map(lambda x: VAL[x],l)))
        row = bin_to_dec(bin[:7])
        col = bin_to_dec(bin[7:])
        val = row * 8 + col
        out = max(out,val)
    return out

def part_two(inp):
    lst = []
    for l in inp:
        bin = ''.join(list(map(lambda x: VAL[x],l)))
        row = bin_to_dec(bin[:7])
        col = bin_to_dec(bin[7:])
        val = row * 8 + col
        lst.append(val)
    lst.sort(reverse=True)
    print(lst)
    prev_i = lst[0]
    for i in lst:
        if prev_i-i>1:
            return i+1
        prev_i = i

if __name__=='__main__':
    inp = sys.stdin.read()
    print(inp)    

    out_1 = part_one(inp.split('\n'))
    print(f'Part one: {out_1}')

    out_2 = part_two(inp.split('\n'))
    print(f'Part two: {out_2}')