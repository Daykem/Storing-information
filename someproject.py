import math
import csv

# Function for get the average of a lists   
def averageOfList(num):
    sumOfNumbers = 0
    for t in num:
        sumOfNumbers = sumOfNumbers + t
    avg = sumOfNumbers / len(num)
    return avg

# Function for get the variance of a lists   
def variance(data, ddof=0):
    n = len(data)
    mean = sum(data) / n
    return sum((x - mean) ** 2 for x in data) / (n - ddof)

# Function for get the standard déviation of a lists   
def stdev(data):
    var = variance(data)
    std_dev = math.sqrt(var)
    return std_dev


# path of database file
f = "database.txt"

# Top of the table
d = {'': ['Design','Implementation','Testing', "Documentation"]}

# Top of the table for csv file
tabcsv = [['', 'Design','Implementation','Testing', "Documentation"]]

# Read database file and stock into object table variable "d"
with open(f, "r") as fp:
    line = fp.readline().strip()
    cnt = 0
    while line:
        a = line.split(" ")
        value = [a[2], a[3], a[4], a[5]]
        line = fp.readline().strip()
        cnt += 1
        d[a[0] + " " + a[1]] = value

# Print table
for k, v in d.items():
    lang, perc, change, doc = v
    print ("{:<18} {:<10} {:<15} {:<11} {:<11}".format(k, lang, perc, change, doc))

# Loop for the application
while (1):
    quest = input ("\nPress a to add new studentGrade, s to get statistic, csv to export csv file, q to quit the program: \n")

    # For Add a new Student with their Grades
    if (quest == "a"):
        name = input ("Add firstname lastname : ")
        design = input ("Add Design grades : ")
        implementation = input ("Add Implementation grades : ")
        testing = input ("Add Testing grades : ")
        documentation = input ("Add Documentation grades : ")
        add_note = "\n"+ name + " " + design + " " + implementation + " " + testing + " " + documentation + ""

        # Add on database
        f = open("database.txt", "a")
        f.write(add_note)

        f = "database.txt"
        d = {'': ['Design','Implementation','Testing', "Documentation"]}

        # Refresh table
        with open(f, "r") as fp:
            line = fp.readline().strip()
            cnt = 0
            while line:
                a = line.split(" ")
                value = [a[2], a[3], a[4], a[5]]
                line = fp.readline().strip()
                cnt += 1
                d[a[0] + " " + a[1]] = value

        # Display Table
        for k, v in d.items():
            lang, perc, change, doc = v
            print ("{:<18} {:<10} {:<15} {:<11} {:<11}".format(k, lang, perc, change, doc))

        # Display statistics
    if (quest == "s"):
        filename = "database.txt"
        statistique = {'': ['Average','Standard Deviation','Minimum Grade', "Maximum Grade"]}

        # Calc statistics
        with open(filename, "r") as fp:
            line = fp.readline().strip()
            cnt = 0
            while line:
                a = line.split(" ")
                tab = [int(a[2]), int(a[3]), int(a[4]), int(a[5])]
                average = round(averageOfList(tab), 3)
                standard = round(stdev(tab), 3)
                minG = min(tab)
                maxG = max(tab)
                value = [average, standard, minG, maxG]
                line = fp.readline().strip()
                cnt += 1
                statistique[a[0] + " " + a[1]] = value

        # Display statistics
        for k, v in statistique.items():
            lang, perc, change, doc = v
            print ("{:<15} {:<9} {:<20} {:<15} {:<11}".format(k, lang, perc, change, doc))

    # Refresh csv file
    if (quest == "csv"):
        tabcsv = [['', 'Design','Implementation','Testing', "Documentation"]]
        with open(f, "r") as fp:
            line = fp.readline().strip()
            cnt = 0
            while line:
                a = line.split(" ")
                value = [a[2], a[3], a[4], a[5]]
                linecsv = [a[0] + " " + a[1], a[2], a[3], a[4], a[5]]
                tabcsv.append(linecsv)
                line = fp.readline().strip()
                cnt += 1
        with open('list.csv', 'w') as filecsv:
            write = csv.writer(filecsv)
            write.writerows(tabcsv)

    # Quit the program
    if (quest == "q"):
        exit(0)