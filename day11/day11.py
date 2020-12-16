import sys
import numpy as np

def part_one(inp):
    def get_num_occupied_neighbours(grid,i,j):
        c = 0
        for x in [-1,0,1]:
            for y in [-1,0,1]:
                if (0<=i+x<grid.shape[0]) and (0<=j+y<grid.shape[1]):
                    if grid[i+x,j+y]==1:
                        c += 1
        return c

    def compute(grid):
        out = grid.copy()
        row, col = out.shape
        for i in range(row):
            for j in range(col):
                if (grid[i,j]==0) and (get_num_occupied_neighbours(grid,i,j)==0):
                    out[i,j] = 1
                elif (grid[i,j]==1) and (get_num_occupied_neighbours(grid,i,j)>=5):
                    out[i,j] = 0
        return out
    state = inp
    next_state = state
    while True:
        state = next_state
        # print('cur state:',state)
        next_state = compute(state)
        # print('next state:',next_state)
        if (state==next_state).all():
            break
        # break
    out = np.sum(np.where(state==1,1,0))
    return out

def part_two(inp):
    def count_direction(grid,i,j,y,x):
        # print(grid)
        row, col = grid.shape
        
        if (x!=0) and (y!=0):
            for (p,q) in zip(range(y,(row+1)*y,y),range(x,(col+1)*x,x)):
                # print(p,q)
                if (i+p==-1) or (i+p==row) or (j+q==-1) or (j+q==col):
                    return 0
                if grid[i+p,j+q]!=-1:
                    return grid[i+p,j+q]

        if y!=0:
            for p in range(y,(row+1)*y,y):
                if (i+p==-1) or (i+p==row):
                    # print('seat not found')
                    return 0
                if grid[i+p,j]!=-1:
                    # print('found seat at pos', (i+p,j))
                    # print(grid[i+p,j])
                    return grid[i+p,j]
                
        if x!=0:
            for q in range(x,(col+1)*x,x):
                if (j+q==-1) or (j+q==col):
                    return 0
                if grid[i,j+q]!=-1:
                    return grid[i,j+q]
                

        

    def get_num_occupied(grid,i,j):
        c = 0
        row, col = grid.shape
        for (y,x) in [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]:
            c += count_direction(grid,i,j,y,x)
        return c

    def compute(grid):
        out = grid.copy()
        row, col = out.shape
        for i in range(row):
            for j in range(col):
                if (grid[i,j]==0) and (get_num_occupied(grid,i,j)==0):
                    out[i,j] = 1
                elif (grid[i,j]==1) and (get_num_occupied(grid,i,j)>=5):
                    out[i,j] = 0
        return out
    # print(grid)
    # for (y,x) in [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]:
    #     print(count_direction(grid,4,3,y,x))
    # print(count_direction(grid,4,3,-1,-1))
    # print(count_direction(grid,1,3,0,1))
    state = inp
    next_state = state
    while True:
        state = next_state
        # print('cur state:',state)
        next_state = compute(state)
        # print('next state:',next_state)
        if (state==next_state).all():
            break
        # break
    out = np.sum(np.where(state==1,1,0))
    return out

if __name__=='__main__':
    inp = sys.stdin.read()
    inp = inp.strip().split('\n')
    grid = np.zeros([len(inp),len(inp[0])])
    for i,l in enumerate(inp):
        for j,c in enumerate(l):
            if c =='.':
                grid[i,j] = -1
            if c=='#':
                grid[i,j] = 1
    print(grid)
    # exit()
    out_1 = part_one(grid)
    print(f'Part one: {out_1}')

    out_2 = part_two(grid)
    print(f'Part two: {out_2}')