def find_max_string(list_of_strings):
	max_length = 0
	output = None
	for each in list_of_strings:
		length = len(each)
		if length > max_length:
			output = each
			max_length = length
	print(output)
	return output



find_max_string(["hi","bye","nowaynohow"])

find_max_string([])