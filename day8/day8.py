import sys

# OPS = {'nop':lambda arg,acc,i:None,
#         'acc':lambda arg,acc,i: acc+=arg,
#         'jmp':lambda arg,acc,i: i+=arg-1}


def part_one(inp):
    global acc,i
    acc = 0
    s = set()
    i = 0
    def computer(op,arg):
        global acc,i
        if op=='nop':
            pass
        if op=='acc':
            acc += arg
        if op=='jmp':
            i += arg-1
        return
    
    while True:
        if i in s:
            break
        s.add(i)
        op, arg = inp[i].split()
        computer(op, int(arg))
        i += 1

    return acc

def part_two(inp):
    global i,acc,s
    acc = 0
    s = set()
    i = 0
    def computer(op,arg):
        global i,acc
        if op=='nop':
            pass
        if op=='acc':
            acc += arg
        if op=='jmp':
            i += arg-1
        return
    # while True:
    #     if i in s:
    #         break
    #     s.add(i)
    #     op, arg = inp[i].split()
    #     computer(op, int(arg))
    #     i += 1

    # return acc
    SW = {'nop':'jmp','jmp':'nop'}
    # evaluate the program first
    def evaluate(j,inp,switch=False):
        global i,acc,s
        i = j
        while True:
            if (i in s) and (i!=j):
                print('LOOP FOUND!')
                return False
            if len(inp[i])==0:
                print('TERMINATE!')
                return True
            s.add(i)
            op, arg= inp[i].split()
            if switch and (i==j):
                op = SW[op]
            computer(op, int(arg))
            i += 1
            print('next i:',i)
            
        # return s
    # seq = evaluate(i,inp,s)
    # j=0
    # evaluate(j,inp)
    # return acc
    evaluate(0,inp)
    
    seq = list(s)
    for j in seq:
        if inp[j].split()[0] in ['nop','jmp']:
            print(j,inp[j].split()[0])
            if evaluate(j,inp,True):
                acc = 0
                s = set()
                print(inp[j])
                inp[j] = SW[inp[j][:3]] + ' ' + inp[j].split()[1]
                print(inp[j])
                evaluate(0,inp)
                return acc


if __name__=='__main__':
    inp = sys.stdin.read()

    out_1 = part_one(inp.split('\n'))
    print(f'Part one: {out_1}')

    out_2 = part_two(inp.split('\n'))
    print(f'Part two: {out_2}')