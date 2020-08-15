
def spiral_order(matrix):

	result = []
	Rows = len(matrix)
	Columns = len(matrix[0])


	for item in matrix[0]:
		print(f'item is {item}')
		result.append(item)
		matrix[0].pop(0)
		print(f'result is{result} and matrix is {matrix}')


	# for each row, increasing, pop last index and append until no next row

	# on last row traverse backwards until at 0 or no next

	# traverse up at index 0

	# call function again and add to previous result 



spiral_order([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]])