numSiblings = int(raw_input("How many siblings do you have? "))

if  numSiblings == 0:
    print "You are an only child"
elif numSiblings >=1 and numSiblings <= 3:
    print "Not too many"
elif numSiblings >3:
    print "Lots of people!"
else:
    print "Must enter a positive integer"
