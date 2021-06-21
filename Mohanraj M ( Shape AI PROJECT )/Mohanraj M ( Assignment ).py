print("-----------Check Leaf or Non-Leap year--------------------")
year=int(input("Enter Your Year:"))

def check(year):
    if (year%4==0 and year%100==0 and year%400==0):
        print("{0} is the Leap Year".format(year))
    else:
        print ("{0} is not a Leap Year".format(year))

check(year)
