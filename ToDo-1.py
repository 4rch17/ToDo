def load_list(the_list): 
	try:
		with open('data_todo_list'):pass
	except IOError:
		return(-1)
	
	# add code if file exists, use toDoList to add items
	return(1)

def save_list(the_list):
	print the_list

	the_file = open('data_todo_list', 'w')

	for item_i in the_list:
		the_file.write(str(item_i[0])+" "+ str(item_i[1])+" "+ str(item_i[2])+" "+ str(item_i[3])+"\n")
		the_file.write(str(item_i[4])+"\n")

	the_file.close()

def add_item(the_list):
	
#
#	type_i
#		Date Specific	- 1
#		Day Specific	- 2
#		None		- 0
#
#	date_i
#		Yes		- YYYYMMDD (20130520)
#		No		- 0
#	
#	day_i
#		Yes		- 1-7 (MON:1, TUE:2, WED:3, THU:4, FRI:5, SAT:6, SUN:7)
#		No		- NA
#
#	time_i
#		Yes		- HHMM (2315)
#		No		- 0
#
#	repeat_i
#		Yes		- 1
#		No		- 0
#
#	desp_i
#		String
#
	day_num = {"MON": 1, "TUE": 2, "WED": 3, "THU": 4, "FRI": 5, "SAT": 6, "SUN": 7} 

	type_i = raw_input('\tInput Type of Event (None = n,N,0 / Date = D,1 / Day = d,2): ')
	if type_i == 1 or type_i == 'D':
		d_i = raw_input('\tInput Date (YYYYMMDD): ')
		time_i = raw_input('\tInput Time (HHMM/0 = not): ')
		repeat_i = raw_input('\tDoes the event repeat? (r,1 = repeats/0 = not: ')
	elif type_i == 2 or type_i == 'd':
		d_i == 0
		while d_i == 0:
			temp_d_i = raw_input('\tInput Day in Week (ddd, e.g. MON TUE): ) ') 
			try:
				d_i = day_num[temp_d_i]
			except KeyError:
				d_i = 0
			
		time_i = raw_input('\tEnter Time (HHMM/0 = not): ')
		repeat_i = raw_input('\tEnter Type (r,1 = repeats/0 = not: ')
	else:
		d_i = 0
		time_i = 0
		repeat_i = 0
	desp_i = raw_input("\tEnter Description: ")
	the_list.append([type_i, d_i, time_i, type_i, repeat_i, desp_i])

todo_list = []

input_u = 'none'

load_var = load_list(todo_list)

while input_u != 'exit':
	if load_var == -1:
		print 'No ToDo Items! Add new item OR input \'help\' to know how to'

	load_var = 0

	input_u = raw_input('input@USER$ ')
	if input_u == 'add':
		add_item(todo_list)
	elif input_u == 'mod':
		mod_i()

save_list(todo_list)

