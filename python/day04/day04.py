import os
import time
import heapq
import re
from math import floor


def main():
    # input
    print(os.getcwd())
    day = "04"
    year = "2023"
    input_file = f"inputs/day{day}.txt"
    print(input_file)
    part1, part2 = 0, 0
    with open(input_file) as f:
        lines = f.read().splitlines()

    start_time = time.time()
    
    # calc
    cards = [1] * len(lines)
    for k, l in enumerate(lines):
        w, y = l.split(":")[1].split("|")
        ws = set([int(i.strip()) for i in w.strip().split(" ") if i.isdigit()])
        ys = set([int(i.strip()) for i in y.strip().split(" ") if i.isdigit()])
        numberWinningCards = len(ws.intersection(ys))
        pointsWinningCards = floor(pow(2, numberWinningCards - 1))
        for j in range(1, numberWinningCards + 1):
            cards[k + j] += cards[k]
        part1 += pointsWinningCards
    part2 = sum(cards)
    
    # output
    duration = int((time.time() - start_time) * 1000000)
    header = "#" * 20
    print(
        f"{header}\n*AoC {year} - Day {day} *\n{header}\n\nPart 1:\t{part1}\nPart 2:\t{part2}\nTime:\t{duration // 1000} ms"
    )


if __name__ == "__main__":
    main()
