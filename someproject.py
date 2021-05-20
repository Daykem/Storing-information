
import math

def averageOfList(num):
    sumOfNumbers = 0
    for t in num:
        sumOfNumbers = sumOfNumbers + t

    avg = sumOfNumbers / len(num)
    return avg

# We relay on our previous implementation for the variance
def variance(data, ddof=0):
    n = len(data)
    mean = sum(data) / n
    return sum((x - mean) ** 2 for x in data) / (n - ddof)

def stdev(data):
    var = variance(data)
    std_dev = math.sqrt(var)
    return std_dev


f = "database.txt"
d = {'': ['Design','Implementation','Testing', "Documentation"]}

with open(f, "r") as fp:
    line = fp.readline().strip()
    cnt = 0
    while line:
        a = line.split(" ")
        value = [a[2], a[3], a[4], a[5]]
        line = fp.readline().strip()
        cnt += 1
        d[a[0] + " " + a[1]] = value

for k, v in d.items():
    lang, perc, change, doc = v
    print ("{:<18} {:<10} {:<15} {:<11} {:<11}".format(k, lang, perc, change, doc))
    
while (1):

    quest = input ("\nPress a to add new studentGrade, s to get statistic, q to quit the program: \n")

    if (quest == "a"):
        name = input ("Add firstname lastname : ")
        design = input ("Add Design grades : ")
        implementation = input ("Add Implementation grades : ")
        testing = input ("Add Testing grades : ")
        documentation = input ("Add Documentation grades : ")
        add_note = "\n"+ name + " " + design + " " + implementation + " " + testing + " " + documentation + ""

        f = open("database.txt", "a")
        f.write(add_note)

        f = "database.txt"
        d = {'': ['Design','Implementation','Testing', "Documentation"]}

        with open(f, "r") as fp:
            line = fp.readline().strip()
            cnt = 0
            while line:
                a = line.split(" ")
                value = [a[2], a[3], a[4], a[5]]
                line = fp.readline().strip()
                cnt += 1
                d[a[0] + " " + a[1]] = value

        for k, v in d.items():
            lang, perc, change, doc = v
            print ("{:<18} {:<10} {:<15} {:<11} {:<11}".format(k, lang, perc, change, doc))

    if (quest == "s"):
        filename = "database.txt"
        statistique = {'': ['Average','Standard Deviation','Minimum Grade', "Maximum Grade"]}

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

        for k, v in statistique.items():
            lang, perc, change, doc = v
            print ("{:<15} {:<9} {:<20} {:<15} {:<11}".format(k, lang, perc, change, doc))

    if (quest == "q"):
        exit(0)
    

