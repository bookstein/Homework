def produce_report(day_count, my_file):
    print "Day ", day_count
    my_file = open(my_file)

    for line in my_file:
        line = line.rstrip()
        words = line.split(',')

        melon = words[0]
        count = words[1]
        amount = words[2]

        report = "Delivered %s %ss for a total of: $%s" % (count, melon, amount)
        print report.upper()

    my_file.close()
    print "\n",


def run_report_on_files():
    file_list = ["um-deliveries-20140519.csv", "um-deliveries-20140520.csv", "um-deliveries-20140521.csv"]
    day_count = 1
    for i in file_list:
        produce_report(day_count, i)
        day_count += 1

if __name__ == "__main__":
    main()