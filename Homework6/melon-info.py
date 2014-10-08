"""
melon_info.py - Prints out all the melons in our inventory

"""

from melons import melon_data



def print_melon(key, data_requests):
	data = []
	for request in data_requests:
		data.append(melon_data[key].get(request, "Sorry, that is not a valid key"))

	# for key in melon_data.keys():
		# if melon_data[key]["seedless"]:
		# 	hasorhasnot = "doesn't have"
		# else:
		# 	hasorhasnot= "has"
		print "%rs %r seeds and are $%r" % (key, data[0], data[2])



if __name__ == '__main__':
    data_requests = ["seedless", "price"]

    for key in melon_data.keys():
        print_melon(key, data_requests)

