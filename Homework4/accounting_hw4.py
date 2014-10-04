def check_customer_balance(orders_file):
	file = open(orders_file)

	MELON_PRICE = 1.00

	for line in file:
		customer_data = line.split(",")
		#print customer_data

		melons_purchased = int(customer_data[2])
		#print melons_purchased
		amount_owed = float(melons_purchased * MELON_PRICE)
		#print amount_owed
		amount_paid = float(customer_data[-1])
		#print amount_paid
		customer_name = customer_data[1]

		# why didn't amount_owed < amount_paid work???? (if code block never ran)
		if amount_owed != amount_paid:
		 	print "%s still has a balance of $%.2f for the purchase of %d melons!" % (customer_name, amount_owed - amount_paid, melons_purchased)

def main():
	check_customer_balance("customer_orders.csv")

if __name__ == "__main__":
	main()