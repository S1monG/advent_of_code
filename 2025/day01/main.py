
def p1():
    count = 0
    dial = 50
    with open('input.txt') as f:
        for line in f.readlines():
            line = line.strip()
            if (line[0] == 'R'):
                dial += int(line[1:]) 
            else:
                dial -= int(line[1:]) 
                
            dial = dial % 100
            if dial == 0:
                count += 1

    return count

def p2():
    count = 0
    dial = 50
    
    with open('input.txt') as f:
        for line in f.readlines():
            line = line.strip()
            steps = int(line[1:])
            if line[0] == 'R':
                count += (dial + steps) // 100
                dial = (dial + steps) % 100
            else:
                if dial - steps < 0:
                    count += abs((100 + dial - steps) // 100)
                    if dial != 0: 
                        count += 1
                dial = (dial - steps) % 100
                count += dial == 0
        
        return count

if __name__ == '__main__':
    print(f"Part 1: {p1()}")
    print(f"Part 2: {p2()}")