from pprint import pprint
from typing import *


def day1_part1(all_int_lines: List[int]) -> None:
	year = 2020

	for idx1, el1 in enumerate(all_int_lines):
		for el2 in all_int_lines[idx1+1:]:

			if el1 + el2 == year:
				print(el1, el2, el1 * el2)
	


def day1_part2(all_int_lines: List[int]) -> None:
	year = 2020

	for idx1, el1 in enumerate(all_int_lines):
		for idx2, el2 in enumerate(all_int_lines[idx1+1:]):
			for el3 in all_int_lines[idx2+1:]:

				if el1 + el2 + el3 == year:
					print(el1, el2, el3, el1 * el2 * el3)




if __name__ == "__main__":

	all_int_lines: List[int] = []

	with open('../input/day1.txt', 'r') as f:
		for line in f:
			line = int(line.strip('\n'))
			all_int_lines.append(line)

	print(len(all_int_lines))
	day1_part1(all_int_lines)
	day1_part2(all_int_lines)
	