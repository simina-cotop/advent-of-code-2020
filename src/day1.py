from pprint import pprint
from typing import *


def day1_part1(all_int_lines: List[int]) -> None:
	year = 2020

	'''for idx, el in enumerate(all_int_lines):
		diff = year - el
		if diff in all_int_lines:
			print(el, diff, el*diff)'''

	for idx1, el1 in enumerate(all_int_lines):
		for idx2 in range(idx1+1, len(all_int_lines)):
			if el1 + all_int_lines[idx2] == year:
				print(el1, all_int_lines[idx2], el1*all_int_lines[idx2])
	


def day1_part2(all_int_lines: List[int]) -> None:
	year = 2020

	for idx1, el1 in enumerate(all_int_lines):
		for idx2 in range(idx1+1, len(all_int_lines)):
			for idx3 in range(idx2+1, len(all_int_lines)):
				if el1 + all_int_lines[idx2] + all_int_lines[idx3] == year:
					print(el1, all_int_lines[idx2], + all_int_lines[idx3], el1*all_int_lines[idx2]*+ all_int_lines[idx3])




if __name__ == "__main__":

	all_int_lines: List[int] = []

	with open('../input/day1.txt', 'r') as f:
		for line in f:
			line = int(line.strip('\n'))
			all_int_lines.append(line)

	print(len(all_int_lines))
	day1_part1(all_int_lines)
	day1_part2(all_int_lines)
	