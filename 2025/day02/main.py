
def invalid1(num):
    s = str(num)
    l = len(s)
    if (l % 2 != 0):
        return False
    return s[:l//2]*2 == s

def invalid2(num):
    s = str(num)
    l = len(s)
    for i in range(1, (l // 2) + 1):
        if (l % i != 0):
            continue
        if (s[:i] * (l//i) == s):
            return True
    return False


def p1p2():
    count1 = 0
    count2 = 0
    with open('input.txt') as f:
        line = f.readlines()[0]
        ranges = line.split(",")
        ranges = [range(int(r.split("-")[0]), int(r.split("-")[1]) + 1) for r in ranges]
        for r in ranges:
            for num in r:
                if (invalid1(num)):
                    count1 += num
                if (invalid2(num)):
                    count2 += num
    
    return count1, count2
        

if __name__ == "__main__":
    p1, p2 = p1p2()
    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")