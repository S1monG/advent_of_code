
def check_accessible(grid, r, c):
    if grid[r][c] == '.':
        return 0
    count = 0
    count += 1 if r > 0 and c > 0 and grid[r-1][c-1] == '@' else 0
    count += 1 if c > 0 and grid[r][c-1] == '@' else 0
    count += 1 if r < len(grid)-1 and c > 0 and grid[r+1][c-1] == '@' else 0
    count += 1 if r > 0 and grid[r-1][c] == '@' else 0
    count += 1 if r < len(grid)-1 and grid[r+1][c] == '@' else 0
    count += 1 if r > 0 and c < len(grid[r])-1 and grid[r-1][c+1] == '@' else 0
    count += 1 if r < len(grid)-1 and c < len(grid[r])-1 and grid[r+1][c+1] == '@' else 0
    count += 1 if c < len(grid[r])-1 and grid[r][c+1] == '@' else 0
    return 1 if count < 4 else 0

def p1():
    accessible = 0
    grid = []
    with open("test.txt") as f:
        for line in f.readlines():
            grid.append(line.strip())
        
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                accessible += check_accessible(grid, r, c)

    return accessible

def p2():
    grid = []
    with open("test.txt") as f:
        for line in f.readlines():
            grid.append(line.strip())
        
    rows = len(grid)
    cols = len(grid[0])
    acc = 0
    while(True):
        accessible = 0
        new_grid = grid.copy()
        for r in range(rows):
            for c in range(cols):
                if (check_accessible(grid, r, c)):
                    accessible += 1
                    new_grid[r] = new_grid[r][:c] + '.' + new_grid[r][c+1:]
        if accessible:
            acc += accessible
            grid = new_grid
        else:
            return acc
        

if __name__ == "__main__":
    print(f"Part 1: {p1()}")
    print(f"Part 2: {p2()}")