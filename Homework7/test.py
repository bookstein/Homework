def test(date):
	f = open('test_customers.csv', 'r+')
	header = f.readline().rstrip().split(",") # on first line in file
	print header



	for line in iter(f.readline,""):
		pos = f.tell()
		data = line.rstrip().split(",")
		# called_or_not gets last item in that array (date of call, or nothing)
		called_or_not = data[-1]
		if len(called_or_not) == 0:
			pos = f.tell()
			called_or_not = date
			new_line = data.append(called_or_not)
			f.seek(pos)
			f.write("".join(data))

		# f.write("".join(data)) # this wrote "Called" over the start of every line


	# for line in iter(f.readline, ''):
	# 	pos = f.tell()
	# 	# data = line.rstrip().split(",")
	# 	f.seek(pos)
	# 	f.write("Called!")



	# modified = f.read()
	# print modified
	f.close()
if __name__ == "__main__":
	test("10/12/14")