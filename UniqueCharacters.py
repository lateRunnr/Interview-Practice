

def check_unique(input_string):
	"""
	Function to check unique characters in a string
	"""
	character_map={}
	for character in input_string:
		if character not in character_map:
			character_map[character] = 1
		else:
			return False
	return True


def main():
	input_string = raw_input("Enter string to test: ")
	if (check_unique(input_string.lower())):
		print "String is unique"
	else:
		print "String is not unique"



if __name__ == '__main__':
	main()