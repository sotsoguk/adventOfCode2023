import os
import time
import heapq
import re
from math import floor, ceil, sqrt





def main():
    # input
    print(os.getcwd())
    day = "08"
    year = "2023"
    input_file = f"inputs/day{day}.txt"
    print(input_file)
    part1, part2 = 0, 0
    with open(input_file) as f:
        lines = f.read().splitlines()

    start_time = time.time()

    tree = {}
    instructions = lines[0]
    print(instructions)
    for l in lines[2:]:
        n, inst = l.split("=")
        n = n.strip()
        l,r = inst.split(",")
        l = l[2:]
        r = r[1:4]
        tree[n] = [l,r]
    
    print(tree)
    currNode = 'AAA'
    steps = 0
    cnt = 0
    while currNode != 'ZZZ':
        command = instructions[cnt]
        if currNode == 'ZZZ':
            break
        if command == 'L':
            currNode = tree[currNode][0]
        else:
            currNode = tree[currNode][1]
        steps += 1
        cnt = (cnt +1) % len(instructions)
    print(steps)
    # output
    duration = int((time.time() - start_time) * 1000000)
    header = "#" * 20
    print(
        f"{header}\n*AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms"
    )


if __name__ == "__main__":
    main()
