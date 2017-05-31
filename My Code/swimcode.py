import time
import random
name = raw_input("What is your name? " )
fifty_time_string = raw_input("How many seconds does it take you to swim 50yd freestyle? ")
fifty_time_flt = float(fifty_time_string)
fifty_time_int = int(fifty_time_string)
goal_thousand_seconds = (fifty_time_flt)**2
goal_thousand_minutes = goal_thousand_seconds/60
print "Your goal is to swim 1000yd freestyle in " + str(goal_thousand_minutes) + " minutes"
print "You will now be selected to swim with a group..."
if goal_thousand_minutes <= 15:
    group = "Gold"
elif goal_thousand_minutes >15 and goal_thousand_minutes < 18:
    group = "Black"
else:
    group = "Purple"
time.sleep(3)
print "You have been selected to join the " + group + " group. Congrats!!"
time.sleep(1)
print "Let's have a look at your teammates results from today"
rand1 = random.randint(20,40)
rand2 = random.randint(20,40)
rand3 = random.randint(20,40)
rand4 = random.randint(20,40)
rand5 = random.randint(20,40)
rand6 = random.randint(20,40)
team_times = {'Jason': rand1, 'Alex': rand2, 'Jasmine': rand3, 'Karen': rand4, 'Jack':rand5}
print team_times
time.sleep(2)
print "Now let's see what you can do."
time.sleep(2)
print "I will count down from your 50 free time and see if you finish before 0."
time.sleep(2)
print "On your mark.."
time.sleep(1)
print "Get set..."
time.sleep(1)
print "GO!"
time.sleep(1)
countdown = fifty_time_int
while countdown  >= 0:
    print countdown
    countdown = countdown - 1
    time.sleep(1)
'''
for countdown in range(fifty_time_int, 0, -1):
    print str(countdown)
    time.sleep(1)
'''
print "You said your best time is " + fifty_time_string + " seconds."
time.sleep(1)
print "You got " + str(rand6) + " seconds."
time.sleep(1)
if rand6 < fifty_time_int:
    print "You beat your time!!!"
else:
    print "Good try, we will work on this more later"
time.sleep(1)
print "Great job today " + name + "! Welcome to the team!"
