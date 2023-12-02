# Challenge Description: https://adventofcode.com/2023/day/1
# Part Two
import regex as re

puzzle = open("input.txt", "r") # Add the puzzle input
lines = puzzle.readlines()

numlst  = []
pattern = re.compile(r"[0-9]|one|two|three|four|five|six|seven|eight|nine")

def getInt(s):
  match s:
    case "one":
      return 1
    case "two":
      return 2
    case "three":
      return 3
    case "four":
      return 4
    case "five":
      return 5
    case "six":
      return 6
    case "seven":
      return 7
    case "eight":
      return 8
    case "nine":
      return 9
    
  return s

for x in lines:
  lst = pattern.findall(x,overlapped=True) # Allow overlapped for cases like oneight
  num1 = getInt(lst[0])
  num2 = getInt(lst.pop())
  num = int(f"{num1}{num2}")
  numlst.append(num)

print(sum(numlst))


