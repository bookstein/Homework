def main():
	my_file = open("um-server-01.log")
	for line in my_file:
		line = line.rstrip() #removes trailing whitespace from end of line
		day = line[0:3]
		if day == "Mon":
			print line

main() # this executes the function whether or not it's run from
#the command line or by importing startercode1