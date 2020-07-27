
def Clock(from_time, to_time):
	from_time = from_time.split(":")
	to_time = to_time.split(":")
	num_changes = 0

    hr_diff =  abs(int(setTime[0])-int(timeToSet[0]))

	from_min = int(setTime[1])
	to_min = int(timeToSet[1])
	min_diff = abs(from_min - to_min)


	if hr_diff > 12:
		num_changes += 24 - hr_diff

	else:
		num_changes += hr_diff


	if min_diff > 30:
		num_changes += 60 - min_diff

	else:
		num_changes += min_diff

	return num_changes






def digit_diff(n):
    str_num = str(n)
    even_total = 0
    odd_total = 0

    for num in str_num:
        if int(num) % 2 == 0:
            even_total = even_total + int(num)
        
        else:
            odd_total = odd_total + int(num)

    diff = even_total - odd_total

    return diff