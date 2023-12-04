import os
import time
import heapq
import re
from math import floor


def game1(game):
    rmax = 12
    gmax = 13
    bmax = 14
    for g in game:
        if g[0] > rmax or g[1] > gmax or g[2] > bmax:
            return False
    return True


def game2(game):
    rmin = 0
    gmin = 0
    bmin = 0
    for g in game:
        rmin = max(rmin, g[0])
        gmin = max(gmin, g[1])
        bmin = max(bmin, g[2])
    return rmin * gmin * bmin


def main():
    # input
    print(os.getcwd())
    day = "02"
    year = "2023"
    input_file = f"inputs/day{day}.txt"
    print(input_file)
    part1, part2 = 0, 0
    with open(input_file) as f:
        lines = f.read().splitlines()
    start_time = time.time()

    # calc
    for num, l in enumerate(lines):
        games = l.split(":")[1].split(";")
        currgame = []
        for g in games:
            gt = [0, 0, 0]
            gc = g.split(",")
            for e in gc:
                if "red" in e:
                    gt[0] = int(re.findall(r"\d+", e)[0])
                if "green" in e:
                    gt[1] = int(re.findall(r"\d+", e)[0])
                if "blue" in e:
                    gt[2] = int(re.findall(r"\d+", e)[0])
            currgame.append(gt)

        if game1(currgame):
            part1 += num + 1
        part2 += game2(currgame)

    # output
    duration = int((time.time() - start_time) * 1000000)
    header = "#" * 20
    print(
        f"{header}\n*AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms"
    )


if __name__ == "__main__":
    main()
