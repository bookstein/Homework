"""
melon_info.py - Prints out all the melons in our inventory

"""

from melons import melon_data



def print_melon(data_requests):
	for request in data_requests:
		data = melon_data.get(request, "Sorry, that is not a valid key")

	# for key in melon_data.keys():
		# if melon_data[key]["seedless"]:
		# 	hasorhasnot = "doesn't have"
		# else:
		# 	hasorhasnot= "has"
		print "%ss %s seeds and are $%0.2f" % (data_requests)



if __name__ == '__main__':
    data_requests = ["name", "seedless", "price"]

    for key in melon_data.keys():
        print_melon(data_requests)

