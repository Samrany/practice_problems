
def spiral_order(matrix):

	result = []

	if matrix:
		for column in matrix[0]:
			result.append(column)

		matrix.pop(0)

	if matrix:
		for row in matrix:
			result.append(row[-1])
			row.pop(-1)


	if matrix:
		for column in matrix[-1][-1::-1]:
				result.append(column)

		matrix.pop(-1)


	if matrix:
		for row in matrix[-1::-1]:
			result.append(row[0])
			row.pop(0)

	if matrix:
		return result + spiral_order(matrix)

	
	else:
		return result

	

	# for each row, increasing, pop last index and append until no next row

	# on last row traverse backwards until at 0 or no next

	# traverse up at index 0

	# call function again and add to previous result 



print(spiral_order([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]))