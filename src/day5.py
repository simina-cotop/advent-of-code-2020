from pprint import pprint
from typing import *

import numpy as np

def read_pass(all_lines: List[str]) -> None:
	all_seat_ids: List[int] = []

	for line in all_lines:
		full_range = list(range(0,128))
		lower_range = list(range(0,8))	

		part1 = line[:7]
		part2 = line[7:]
		#print(part1, part2)
		for el in part1:
			if el == 'F':
				middle = int(len(full_range) / 2)
				full_range = full_range[:middle]
				#print("lower", full_range)
			elif el == 'B':
				middle = int(len(full_range) / 2)
				full_range = full_range[middle:]
				#print("upper", full_range)

		for el in part2:
			if el == 'R':
				middle = int(len(lower_range) / 2)
				lower_range = lower_range[middle:]
				#print("upper2", lower_range, el)
			elif el == 'L':
				middle = int(len(lower_range) / 2)
				lower_range = lower_range[:middle]
				#print("lower2", lower_range, el)

		seat_id = full_range[0] * 8 + lower_range[0]
		#print("Seat ID = ", seat_id)
		all_seat_ids.append(seat_id)
	#print("MAX: ", max(all_seat_ids))
	print("Sorted: ", sorted(all_seat_ids))

	all_ids = list(range(0,952))
	print("res=", set(all_ids) - set(all_seat_ids))








if __name__ == "__main__":

	all_lines: List[str] = []

	with open('../input/day5.txt', 'r') as f:
		for line in f:
			line = line.strip('\n')
			all_lines.append(line)

	#pprint(all_lines)
	test = ['BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']
	#read_pass(test)
	read_pass(all_lines)
