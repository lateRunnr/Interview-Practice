def encode(test_string):
	"""
	Function to compress the string
	e.g: aaaabbccaa = a4b2c2a2
	"""
	count=0
	prev_char=test_string[0]
	encoded_string=""
	for char in test_string:
		if prev_char == char:
			count+=1
		else:
			encoded_string=encoded_string+prev_char+str(count)
			count=1
		prev_char=char
	encoded_string=encoded_string+prev_char+str(count)
	return encoded_string


def main():
	test_string=raw_input("Enter String to encode:  ")
	encoded_string = encode(test_string)
	if len(encoded_string) > len(test_string):
		print "Encoded String:  ", test_string
	else:
		print "Encoded String: ",encoded_string 
if __name__ == '__main__':
	main()