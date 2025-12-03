import numpy as np

def p1():
    joltage = 0
    with open("input.txt") as f:
        banks = [line.strip() for line in f.readlines()]
        for b in banks:
            arr = np.array([int(n) for n in b]) 
            index_max_1 = np.argmax(arr[:-1])
            index_max_2 = np.argmax(arr[index_max_1+1:])
            index_max_2 += index_max_1+1
            joltage += arr[index_max_1] * 10 + arr[index_max_2]
    return joltage

def p2():
    joltage = 0
    with open("input.txt") as f:
        banks = [line.strip() for line in f.readlines()]
        for b in banks:
            j = 0
            idx_max = 0
            arr = np.array([int(n) for n in b], dtype="i8")
            for i in range(0, 12):
                #print(f"array: {arr}, allowed array: {arr[:i-11]}, i: {i}")
                if (i == 11):
                    idx_max = np.argmax(arr)
                else:
                    idx_max = np.argmax(arr[:i-11])
                #print(f"max index: {idx_max}", end="\n\n")
                j = j * 10 + arr[idx_max]
                arr = arr[idx_max+1:]
            joltage += j
    return joltage
            



if __name__ == "__main__":
    print(f"Part 1: {p1()}")
    print(f"Part 2: {p2()}")