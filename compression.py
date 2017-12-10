def decode(map_string):
	"""
	Function to convert hashmap into encoded string
	"""
	compressed_string = ""
	for key in map_string:
		compressed_string=compressed_string + key + str(map_string.get(key))
	return compressed_string


def compress(test_string):
	"""
	Function to compress the string
	e.g: aaaabbcdcd = a4b2c2d2
	"""
	map_string={}
	for char in test_string:
		if char not in map_string:
			map_string[char]=1
		else:
			count=map_string.get(char)
			count+=1
			map_string[char]=count
	compressed_string=decode(map_string)
	return compressed_string
def main():
	test_string=raw_input("Enter String to compress:  ")
	compressed_string = compress(test_string)
	print compressed_string
	if len(compressed_string) > len(test_string):
		print "Compressed String:  ", test_string
	else:
		print "Compressed String: ",compressed_string 
if __name__ == '__main__':
	main()