from typing import *
from pprint import pprint

EXPECTED_FIELDS: List[str] = [
		'byr', 'cid', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid'
	]

EXPECTED_FIELDS2: List[str] = [
		'byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid'
	]

VALID_FIELDS: Dict[str, Tuple[int,int]] = {
	'byr':(1920, 2002),
	'ecl':['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'], 
	'eyr':(2020, 2030), 
	'hcl':(), 
	'hgt':(), 
	'iyr':(2010, 2020), 
	'pid':()
}

def day4_part1(all_lines: List[str]) -> int:
	passport_counter: int = 0
	
	for line in all_lines:
		passport: List[str] = []	
		splitted_line: List[str] = line.replace("\n", " ").split(" ")
		for element in splitted_line:
			splitted_element = element.split(":")
			passport.append(splitted_element[0])

		passport.sort()
		
		if passport == EXPECTED_FIELDS or passport == EXPECTED_FIELDS2:
			passport_counter += 1
	return passport_counter

def day4_part2(all_lines: List[str]) -> int:
	passport_counter: int = 0
	
	for line in all_lines:
		passport: List[str] = []	
		splitted_line: List[str] = line.replace("\n", " ").split(" ")
		for element in splitted_line:
			splitted_element = element.split(":")
			passport.append(splitted_element[0])

		passport.sort()
		
		if passport == EXPECTED_FIELDS or passport == EXPECTED_FIELDS2:
			if 'byr' in range(1920,2002):
			passport_counter += 1
	return passport_counter



if __name__ == "__main__":

	with open('../input/day4.txt', 'r') as f:
		data = f.read()
	
	#print(len(all_data))

# 	data = '''ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
# byr:1937 iyr:2017 cid:147 hgt:183cm

# iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
# hcl:#cfa07d byr:1929

# hcl:#ae17e1 iyr:2013
# eyr:2024
# ecl:brn pid:760753108 byr:1931
# hgt:179cm

# hcl:#cfa07d eyr:2025 pid:166559648
# iyr:2011 ecl:brn hgt:59in
# '''
	all_data: List[str] = data.split('\n\n')
	print(len(all_data))
	p1res = day4_part1(all_data)
	print(p1res)
	#day4_part2(all_lines)