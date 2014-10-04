def count_melon_types():
    """
    Function opens file, loops through file to count melons by type.
    Outputs a dictionary of melons by type.
    """

    #open the file
    f = open("orders_by_type.csv")
    #create a dictionary of key-value pairs, defaults at 0
    melon_tallies = {"Musk": 0, "Hybrid": 0, "Watermelon": 0, "Winter": 0}
    #for each line in file, create array. Melon type item 1. Count, item 2.
    #record new count by updating dictionary
    for line in f:
        data = line.split(",")
        melon_type = data[1]
        melon_count = int(data[2])
        melon_tallies[melon_type] += melon_count

    return melon_tallies
    f.close()

def calc_melon_revenue(melon_tallies):
    """
    Function contains dictionary of melon types and prices.
    Input: melon tally
    Output: revenue, as price * melon count by melon type
    """
    #dictionary with melon prices
    melon_prices = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 }
    #declare var with default value zero
    total_revenue = 0
    #for each melon type in the melon tallies dictionary,
    #calculate revenue by price and number of melons
    for melon_type in melon_tallies:
        price = melon_prices[melon_type]
        revenue = price * melon_tallies[melon_type]
        total_revenue += revenue
        produce_sales_report(melon_tallies[melon_type], melon_type, price, revenue)

def online_or_phone_sales():
    """
    Function breaks data in 2 lists: one for internet orders,
    one for orders by salespeople.
    Each list adds the value of each sale to get the aggregate totals
    for sales calls versus internet orders.
    Finally, it compares the value of the salespeople's list > internet list
    """
    #open file
    f = open("orders_with_sales.csv")
    #create list with default values of 0
    sales = [0, 0]
    #for each line in file, create list "data".
    # if item 1 is 0, add value of float(item 3) to first item in array
    # otherwise add to second value of data array
    for line in f:
        data = line.split(",")
        if data[1] == "0":
            sales[0] += float(data[3])
        else:
            sales[1] += float(data[3])
    return sales

def produce_sales_report(melon_tally, melon_type, price, revenue):
    #generate report for each type of melon
    print "We sold %d %s melons at %0.2f each for a total of %0.2f" % (melon_tally, melon_type, price, revenue)

def produce_revenue_report(salesdata):
    #Summarize sources of revenue by sales data
    print "Salespeople generated %0.2f in revenue." % salesdata[1]
    print "Internet sales generated %0.2f in revenue." % salesdata[0]
    if salesdata[1] > salesdata[0]:
        print "Guess there's some value to those salespeople after all."
    else:
        print "Time to fire the sales team! Online sales rule all!"

def main():
    #create melon tally, produce report
    tallies = count_melon_types()
    calc_melon_revenue(tallies)
    #calc revenue from online_or_phone_sales
    #produce revenue report
    sales_comparison = online_or_phone_sales()
    produce_revenue_report(sales_comparison)



    # f = open("orders_by_type.csv")
    # melon_tallies = {"Musk": 0, "Hybrid": 0, "Watermelon": 0, "Winter": 0}
    # for line in f:
    #     data = line.split(",")
    #     melon_type = data[1]
    #     melon_count = int(data[2])
    #     melon_tallies[melon_type] += melon_count
    # f.close()
    # melon_prices = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 }
    # total_revenue = 0
    # for melon_type in melon_tallies:
    #     price = melon_prices[melon_type]
    #     revenue = price * melon_tallies[melon_type]
    #     total_revenue += revenue
    #     print "We sold %d %s melons at %0.2f each for a total of %0.2f" % (melon_tallies[melon_type], melon_type, price, revenue)
    # print "******************************************"
    # f = open("orders_with_sales.csv")
    # sales = [0, 0]
    # for line in f:
    #     data = line.split(",")
    #     if data[1] == "0":
    #         sales[0] += float(data[3])
    #     else:
    #         sales[1] += float(data[3])
    # print "Salespeople generated %0.2f in revenue." % sales[1]
    # print "Internet sales generated %0.2f in revenue." % sales[0]
    # if sales[1] > sales[0]:
    #     print "Guess there's some value to those salespeople after all."
    # else:
    #     print "Time to fire the sales team! Online sales rule all!"
    # print "******************************************"


if __name__ == "__main__":
    main()
