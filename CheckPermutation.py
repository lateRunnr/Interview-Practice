


def map_string(test_string):
	"""
	Map strings in a Dictionary / Hasp Map
	"""
	string_map={}
	for char in test_string:
		if char not in string_map:
			string_map[char]=1
		else:
			count=string_map.get(char)
			count+=1
			string_map[char]=count
	return string_map

def check_permutation(first_string,second_string):
	"""
	Function to check if two strings are permutations of each other
	"""

	if len(first_string) != len(second_string):
		return False

	## Map first string ##
	mapped_string = map_string(first_string)

	## Comparing second string with first string ##
	for char in second_string:
		if char not in mapped_string:
			return False
		else:
			count=mapped_string.get(char)
			count-=1
			if count == 0:
				del mapped_string[char]
			else:
				mapped_string[char]=count
	return True


def main():
	first_string = raw_input("Enter first String:  ")
	second_string = raw_input("Enter second String: ")
	if(check_permutation(first_string,second_string)):
		print "Strings are permutations of each other"
	else:
		print "Strings are not permutations of each other"

if __name__ == '__main__':
	main()