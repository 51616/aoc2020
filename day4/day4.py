import sys
import re

filter = {'byr':lambda x: 1920<=int(x)<=2002,
            'iyr': lambda x: 2010<=int(x)<=2020,
            'eyr': lambda x: 2020<=int(x)<=2030,
            'hgt': lambda x: (x[-2:] in ['cm','in']) and (150<=int(x[:-2])<=193 if x[-2:]=='cm' else \
                            59<=int(x[:-2])<=76),
            'hcl': lambda x: (x[0]=='#') and (len(x[1:])==6) and (not bool(re.compile('[^0-9a-f]').search(x[1:]))),
            'ecl': lambda x: x in set(['amb','blu','brn','gry','grn','hzl','oth']),
            'pid': lambda x: (len(x)==9) and (x.isdecimal()),
            'cid': lambda x: True,
            }


def part_one(inp):
    fields = set(['byr','iyr','eyr','hgt','hcl','ecl','pid','cid'])
    out = 0
    d = set()
    for l in inp.split('\n'):
        if len(l)>0:
            for f in l.split():
                k,v = f.split(':')
                d.add(k)
        else:
            x = fields.intersection(d)
            if len(x)==len(fields):
                out += 1
            elif (len(x)==len(fields)-1) and ('cid' not in x):
                out += 1
            d = set()
    return out

def part_two(inp):
    fields = set(['byr','iyr','eyr','hgt','hcl','ecl','pid','cid'])
    out = 0
    d = set()
    for l in inp.split('\n'):
        if len(l)>0:
            for f in l.split():
                k,v = f.split(':')
                if filter[k](v):
                    d.add(k)
                # else:
                #     print(f'Invalid field: {k}:{v}')
                #     print()
        else:
            x = fields.intersection(d)
            if len(x)==len(fields):
                out += 1
            elif (len(x)==len(fields)-1) and ('cid' not in x):
                out += 1
            d = set()
    return out


if __name__=='__main__':
    
    inp = sys.stdin.read()

    out_1 = part_one(inp)
    print(f'Part one: {out_1}')

    out_2 = part_two(inp)
    print(f'Part two: {out_2}')