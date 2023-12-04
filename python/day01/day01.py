import os
import time
import heapq
import re

def main():

    # input
    print(os.getcwd())
    day = "01"
    year = "2023"
    input_file = f'inputs/day{day}.txt'
    print(input_file)
    part1, part2 = 0, 0
    with open(input_file) as f:
        lines = f.read().splitlines()
    print(lines)
    start_time = time.time()
    # calc
    for l in lines:
        dl = re.findall("\d",l)
        # print(int("".join([dl[0],dl[-1]])))
        print(dl)
        part1 += int("".join([dl[0],dl[-1]]))
    # output
    duration = int((time.time() - start_time) * 1000000)
    header = "#" * 20
    print(
        f"{header}\n*AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms")


if __name__ == "__main__":
    main()
    
