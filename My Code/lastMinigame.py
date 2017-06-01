import time

print "Welcome to Word Scramble"

print "Player 1, Enter 10 words\n"

n1 = raw_input(" ")
n2 = raw_input(" ")
n3 = raw_input(" ")
n4 = raw_input(" ")
n5 = raw_input(" ")
n6 = raw_input(" ")
n7 = raw_input(" ")
n8 = raw_input(" ")
n9 = raw_input(" ")
n10 = raw_input(" ")

wordlist = []
wordlist.append(n1)
wordlist.append(n2)
wordlist.append(n3)
wordlist.append(n4)
wordlist.append(n5)
wordlist.append(n6)
wordlist.append(n7)
wordlist.append(n8)
wordlist.append(n9)
wordlist.append(n10)

print "Player 2, get ready to memorize your words"
time.sleep(3)
print wordlist
time.sleep(10)

print('\n' * 100)
print raw_input("Player 2, Enter the Words\n")

count = 0
while True:
    guess = raw_input("")
    if guess in wordlist:
            count + 1
            wordlist.remove(guess)
            print "Score: " + str(count)
            #print wordlist

'''
count = 0
timer = 20
while timer  >= 0:
    timer = timer - 1
    time.sleep(1)
    guess = raw_input("")
    if guess in wordlist:
        count + 1
        wordlist.remove(guess)
        print "Score: " + str(count)
    if timer == 0:
        break
        
        print "Game over"
        print "Score: " + count + "/10"
    
'''
