# Name: Mackenzie Duchen
# Period: 4
# Dice Rolling Simulator
import random
selected = random.randint(1,6)
randomNum = random.randint(1,6)
x = int(input("How Many Rolls?: "))
print(selected)
while True:
	printScore()
    print('The dice rolled and you got:')
    x = randomNum
    break
if x < 0:
        x = 0
        print('Negative changed to zero')
    elif x == 0:
          print('Zero')
    elif x == 1:
        print('Single')
    else:
        print('More')


def printScore():
	print("The Score is: ", rolled_num)


