def test():
	f = open('test_customers.csv', 'r+')
	header = f.readline().rstrip().split(",") # on first line in file
	print header

	line = f.readline() # starting after first line
	data = line.rstrip().split(",")
	pos = f.tell()
	print line
	print pos

	for line in iter(f.readline, ''):
		pos = f.tell()
		# data = line.rstrip().split(",")
		f.seek(pos)
		f.write("Called!")


	# called_or_not gets last item in that array (date of call, or nothing)
	# called_or_not = data[-1]
	# print called_or_not
	# called_or_not = "Called"
	# f.write("".join(data))


	# modified = f.read()
	# print modified
	f.close()
if __name__ == "__main__":
	test()