currentYear = 2017
years = raw_input("Input a number of years: ")
futureYear = currentYear+ int(years)
print ("In " + str(years) + " years, it will be the year " + str(futureYear))
if futureYear%3 == 0:
    print "That year is a multiple of 3!!!"
else:
    print "Just another year"

