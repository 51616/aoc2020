import sys
def count(l,x):
    c = 0
    for i in l:
        if i==x:
            c+=1
    return c

def part_one(inp):
    out = 0
    for (mn, mx, ch, pwd) in inp:
        c = count(pwd,ch)
        if mn<=c<=mx:
            out += 1
    return out

def part_two(inp):
    out = 0
    for (mn, mx, ch, pwd) in inp:
        if (pwd[mn-1]==ch) ^ (pwd[mx-1]==ch):
            out += 1
    return out    

if __name__=='__main__':
    inp = sys.stdin.read()
    print(inp.split('\n'))
    # inp = [(i.split('-')[0],i.split('-')[1],) for i in inp.split()]
    l = []
    for i in inp.split('\n'):
        if len(i)>0:
            splt_d = i.split('-')
            mn = int(splt_d[0])
            mx = int(splt_d[1].split()[0])
            ch = splt_d[1].split(':')[0][-1]
            pwd = splt_d[1].split(':')[1][1:]
            l.append((mn,mx,ch,pwd))
    # print(l)
    out_1 = part_one(l)
    print(f'Part one: {out_1}')
    out_2 = part_two(l)
    print(f'Part two: {out_2}')