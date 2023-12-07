import os
import time
import heapq
import re
from math import floor, ceil, sqrt


def calcRace(t, s):
    d = sqrt(t * t - 4 * s)
    delta = 0
    if floor(d) == d:
        delta = int(d - 1)
    else:
        delta = (floor((t + d) / 2) - ceil((t - d) / 2)) + 1
    return delta


def main():
    # input
    print(os.getcwd())
    day = "06"
    year = "2023"
    input_file = f"inputs/day{day}.txt"
    print(input_file)
    part1, part2 = 1, 0
    with open(input_file) as f:
        lines = f.read().splitlines()

    start_time = time.time()

    # process input
    times = [int(i.strip()) for i in lines[0].split(":")[1].split(" ") if i.isdigit()]
    dists = [int(i.strip()) for i in lines[1].split(":")[1].split(" ") if i.isdigit()]

    # part 1
    for t, d in zip(times, dists):
        part1 *= calcRace(t, d)

    # part 2
    timePart2 = int("".join(map(str, times)))
    distancePart2 = int("".join(map(str, dists)))
    part2 = calcRace(timePart2, distancePart2)

    # output
    duration = int((time.time() - start_time) * 1000000)
    header = "#" * 20
    print(
        f"{header}\n*AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms"
    )


if __name__ == "__main__":
    main()
