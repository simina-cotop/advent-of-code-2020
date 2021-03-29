from collections import OrderedDict
from typing import *
from pprint import pprint

EXPECTED_FIELDS: List[str] = [
		'byr', 'cid', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid'
	]

EXPECTED_FIELDS2: List[str] = [
		'byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid'
	]


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

def passport_check(passport: Dict[str,str]) -> bool:
	counting_check = 0
	check = False
	print('NEW')
	for k in passport.keys():
		
		if k == 'byr':
			if len(passport[k]) == 4 and int(passport[k]) in range(1920, 2003):
				print('byr')
				counting_check += 1

		elif k == 'iyr':
			if len(passport[k]) == 4 and int(passport[k]) in range(2010, 2021):
				print('iyr')
				counting_check += 1

		elif k == 'eyr':
			if len(passport[k]) == 4 and int(passport[k]) in range(2020, 2031):
				print('eyr', passport[k])
				counting_check += 1

		elif k == 'hgt':
			if 'cm' in passport[k]:
				if int(passport[k].rstrip('cm')) in range(150, 194):
					print('hgt1')
					counting_check += 1
			elif 'in' in passport[k]:
				if int(passport[k].rstrip('in')) in range(59, 77):
					print('hgt2')
					counting_check += 1

		elif k == 'hcl':
			if passport[k].startswith('#') and len(passport[k].lstrip('#')) == 6:
				print('hcl')
				counting_check += 1

		elif k == 'ecl':
			if passport[k] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
				print('ecl')
				counting_check += 1

		elif k == 'pid':
			if len(passport[k]) == 9:
				print('pid')
				counting_check += 1

	# if 'cid' in passport.keys():
	# 	if counting_check == len(passport) or counting_check == len(passport) - 1:
	# 		check = True
	# else:
	# 	if counting_check == len(passport):
	# 		check = True

	if counting_check == 7:
		check = True
	else:
		print(counting_check, len(passport), passport)

	'''if counting_check == len(passport) or counting_check == len(passport) - 1:
		print(counting_check, len(passport), passport)
		check = True'''
	
	return check

def day4_part2(all_lines: List[str]) -> int:
	passport_counter: int = 0
	
	for line in all_lines:
		passport: Dict[str,str] = OrderedDict()
		splitted_line: List[str] = line.replace("\n", " ").split(" ")
		
		for element in splitted_line:
			splitted_element = element.split(":")
			
			passport[splitted_element[0]] = splitted_element[1]

		new_pass = OrderedDict(sorted(passport.items(), key=lambda t: t[0]))
		
		if list(new_pass.keys()) == EXPECTED_FIELDS or list(new_pass.keys()) == EXPECTED_FIELDS2:
			validity = passport_check(new_pass)
			if validity == True:
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

# 	data = '''pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
# hcl:#623a2f

# eyr:2029 ecl:blu cid:129 byr:1989
# iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

# hcl:#888785
# hgt:164cm byr:2001 iyr:2015 cid:88
# pid:545766238 ecl:hzl
# eyr:2022

# iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719'''

# 	data = '''eyr:1972 cid:100
# hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

# iyr:2019
# hcl:#602927 eyr:1967 hgt:170cm
# ecl:grn pid:012533040 byr:1946

# hcl:dab227 iyr:2012
# ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

# hgt:59cm ecl:zzz
# eyr:2038 hcl:74454a iyr:2023
# pid:3556412378 byr:2007'''

	all_data: List[str] = data.split('\n\n')
	print(len(all_data))
	p1res = day4_part1(all_data)
	print(p1res)
	p2res = day4_part2(all_data)
	print(p2res)