# Challenge Description: https://adventofcode.com/2023/day/1
# Part One
import re

puzzle = open("input.txt", "r") # Add the puzzle input
lines = puzzle.readlines()

numlst  = []
pattern = re.compile("[0-9]")

for x in lines:
  lst = pattern.findall(x)
  num = int(f"{lst[0]}{lst.pop()}")
  numlst.append(num)

print(sum(numlst))