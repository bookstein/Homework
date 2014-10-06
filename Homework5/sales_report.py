"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.

"""

def main():
    #could use a tuple instead of 2 separate lists, since you want the person's record?
    salespeople = []
    melons_sold = []

    f = open("sales_report.csv")
    for line in f:
        line = line.rstrip()
        entries = line.split(",")
        # too many definitions? or is this helpful for clarity? could you do salesperson, melons = entries?
        salesperson = entries[0]
        melons = int(entries[2])

        if salesperson in salespeople:
            # checks if salesperson has already been added to salespeople. Names are repeated on multiple lines.
            # initially, salespeople[] will be empty, but over the course of filling it...
            position = salespeople.index(salesperson)
            # adds melons at corresponding index position
            melons_sold[position] += melons
        else:
            salespeople.append(salesperson)
            melons_sold.append(melons)


    for i in range(len(salespeople)):
        print "%s sold %d melons" % (salespeople[i], melons_sold[i])



if __name__ == "__main__":
    main()