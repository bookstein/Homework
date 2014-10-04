def main():
    my_file = open("um-server-01.log")
    for line in my_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Mon":
            print line

if __name__ == "__main__":
    main()
#this runs the function ONLY if it's run from the command line
#python process.py
#(this statement used by convention)
#one reason to use this convention: to define all the stuff
#your function can do, and then execute it at the bottom, in one place!