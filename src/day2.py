from typing import *



# Example password:
# 1-3 a: abcde
def day2_part1(all_lines: List[str]) -> None:
	correct_password = 0
	for line in all_lines:
		# part1: 1-3 a 
		# part2: abcde
		part1, part2 = line.split(": ")
		# range: 1-3; letter: a 
		range, letter = part1.split(" ")
		# Get the start and the end of the range
		range_start, range_end = (int(range.split("-")[0]), int(range.split("-")[1]))

		letter_count = part2.count(letter)
		# If the number of occurrences of the letter is between range start and end
		if letter_count >= range_start and letter_count <= range_end:
			correct_password += 1
	print("pass1=", correct_password)


def day2_part2(all_lines: List[str]) -> None:
	correct_password = 0
	for line in all_lines:
		
		# part1: 1-3 a 
		# part2: abcde
		part1, part2 = line.split(": ")
		# range: 1-3; letter: a 
		range, letter = part1.split(" ")
		# Get the start and the end of the range
		range_start, range_end = (int(range.split("-")[0]), int(range.split("-")[1]))

		letter_indeces = [idx + 1 for idx, el in enumerate(part2) if el == letter]
		
		# If either range_start or range_end appear in the list, we consider the password to be valid
		if range_start in letter_indeces and range_end not in letter_indeces:
			correct_password += 1
		if range_start not in letter_indeces and range_end in letter_indeces:
			correct_password += 1
		
	print("pass2=", correct_password)






if __name__ == "__main__":

	all_lines: List[str] = []

	with open('../input/day2.txt', 'r') as f:
		for line in f:
			line = line.strip('\n')
			all_lines.append(line)

	#print(len(all_lines))
	day2_part1(all_lines)
	day2_part2(all_lines)