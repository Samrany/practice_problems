
def create_museum(m, n):
	"""creates a two-dimensional array based on the number of rows (m) and number of items in each row(n)"""
	museum = []
	for row in range(m):
		row = []
		for item in range(n):
			row.append("0")
		museum.append(row)

	print(museum) #DELETE AFTERWARDS
	return museum


def print_museum(museum): #DELETE AFTERWARDS
	for sublist in museum:
		output = " "
		for item in sublist:
			output += str(item)

		print(output)


def check_for_unguarded_rooms(museum):
	"""loops over a two-dimensional array and determines if there are any unwatched rooms and returns boolean and unwatched room coordinates"""
	empty_rooms = []

	for row_idx in range(len(museum)):	
		
		for item_idx in range(len(museum[row_idx])): #Go back and fix this to be enumerate instead
			
			if museum[row_idx][item_idx] == "0":
				empty_rooms.append([row_idx, item_idx])

	# for row_idx, row_value in enumerate(museum):
	# 	for item_idx, item_value in enumerate(row):
	# 		if item_value == " ":
	# 			print(item)
	# 			empty_rooms.append([row_idx, item_idx]) # need index

	if not empty_rooms:
		print("true")
	
	else:
		print("false")

		for room in empty_rooms:
			print(str(room[0]) + " " + str(room[1]))


def check_museum_security(size, *args):
	"""TBD"""

	museum = create_museum(size[0], size[1]) #assumes size is a list of 2 elements
	guards = []

#fill the museum w. guards and walls at their appropriate locations and create separate list to hold distinct g's and w's
	for arg in args:
		row, item, designation = arg
		# row = arg[0] #unpack later
		# item = arg[1]
		# designation = arg[2]

		museum[row][item] = designation

		if designation == "g":
			guards.append(arg)
	
	print_museum(museum)
	print("fixing empty rooms to be watched...")

	for guard in guards:
		guard_row_idx = guard[0]
		guard_item_idx = guard[1]

		#check to right
		for curr_item_idx in range(guard_item_idx + 1, len(museum[guard_row_idx]),1):
			if museum[guard_row_idx][curr_item_idx] == "g" or museum[guard_row_idx][curr_item_idx] == "w":
				break

			else:
				museum[guard_row_idx][curr_item_idx] = "-"


		#check left
		for curr_item_idx in range(guard_item_idx-1,-1,-1):
			if museum[guard_row_idx][curr_item_idx] == "g" or museum[guard_row_idx][curr_item_idx] == "w":
				break

			else:
				museum[guard_row_idx][curr_item_idx] = "-"


		#check down
		for curr_row_idx in range(guard_row_idx + 1, len(museum), 1):
		
			if museum[curr_row_idx][guard_item_idx] == "g" or museum[curr_row_idx][guard_item_idx] == "w":
				break

			else:
				museum[curr_row_idx][guard_item_idx] = "-"

		#check up
		for curr_row_idx in range(guard_row_idx - 1, -1, -1):
		
			if museum[curr_row_idx][guard_item_idx] == "g" or museum[curr_row_idx][guard_item_idx] == "w":
				break

			else:
				museum[curr_row_idx][guard_item_idx] = "-"

			
	check_for_unguarded_rooms(museum)
  
# check_museum_security([4, 6],[0, 0, 'g'], [0, 1, 'w'], [1, 1, 'g'], [2, 2, 'w'], [2, 3, 'g'])
# check_museum_security([2, 2],[0, 0, 'g'], [1, 1, 'g'])





