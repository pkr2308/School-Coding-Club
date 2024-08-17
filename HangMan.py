from turtle import *
import random

def drawMan(lineNo):
    if (lineNo == 5):
        right(90)
        circle(35)
    if (lineNo == 4):
        left(90)
        up()
        forward(70)
        down()
        forward(85)
    if (lineNo == 3):
        right(30)
        forward(60)
        right(180)
        forward(60)
        right(120)
    if (lineNo == 2):
        forward(60)
        right(180)
        forward(60)
        right(30)
    if (lineNo== 1):
        forward(55)
        left(130)
        forward(50)
        left(180)
        forward(50)
    if (lineNo== 0):
        right(80)
        forward(50)


mywords=('hello','random','wonderful','holiday','everyday','boring','really','disaster','delicious','ready')
word = mywords[random.randint(0,9)]

lives = 6
prevlives = 6

chars = []

up()
left(180)
forward(70)
left(90)
down()
forward(100)
right(180)
forward(300)
right(90)
forward(150)
right(90)
forward(25)

for i in word:
    if not (i in chars):
        chars.append(i)
vowels = ['a', 'e', 'i', 'o', 'u']
        

for item in vowels:
    if item in chars:
        chars.remove(item)

for letter in word:
    if letter in chars:
        print('__',end=' ')
    else:
        print(letter, end=' ')
                
while(lives > 0):
    user = input("\nWhat's your guess?")
    if not(user in chars):
        lives = lives - 1
        print(f'Bad luck, you have {lives} lives remaining')
        drawMan(lives)
    else:
        chars.remove(user)
        for letter in word:
            if letter in chars:
                print('__',end=' ')
            else:
                print(letter, end=' ')
    if len(chars) == 0:
        print('\nGood job!')
        break
else:
    print('\nBad luck, you lost')



    
