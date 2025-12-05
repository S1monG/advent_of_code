
def p1():
    with open("input.txt") as f:
        lines = f.readlines()
        rs, i = ''.join(lines).split("\n\n")
        ids = i.split("\n")
        rs = [range(int(a.split("-")[0]), int(a.split("-")[1])+1) for a in rs.split("\n")]
        
        fresh = 0
        for i in ids:
            i = int(i)
            for r in rs:
                if (i in r):
                    fresh += 1
                    break
        return fresh
    
def p2():
    with open("input.txt") as f:
        lines = f.readlines()
        rs, i = ''.join(lines).split("\n\n")
        rs = [range(int(a.split("-")[0]), int(a.split("-")[1])+1) for a in rs.split("\n")]
        
        fresh = [] # list of ranges
        for r in rs:
            new_fresh = []
            for fr in fresh:
                if r.stop < fr.start or r.start > fr.stop:
                    new_fresh.append(fr)
                else:
                    if r.start < fr.start:
                        if r.stop >= fr.start:
                            r = range(r.start, max(r.stop, fr.stop))
                        else:
                            new_fresh.append(fr)
                    else:
                        if fr.stop >= r.start:
                            r = range(min(r.start, fr.start), max(r.stop, fr.stop))
                        else:
                            new_fresh.append(fr)
            new_fresh.append(r)
            fresh = new_fresh
        total = 0
        for r in fresh:
            total += r.stop - r.start
        return total






if __name__ == "__main__":
    print(f"Part 1: {p1()}")
    print(f"Part 2: {p2()}")
