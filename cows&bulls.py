#we used random number geneartion for not allowing the repetition.
from random import randint
def random():
    while True:
        #here we taken 3 digits number that's why we take 100 to 999.
        n = str(randint(100,999))
        if not(n[0]==n[1] or n[1]==n[2] or n[0]==n[2]):
            return n
name = input("Welcome to the cows and bulls game\nPlease enter your name.")
print("Hello", name)
chances = 10
cows = 0
bulls = 0
#No repetition that why we used random function.
num = str(random())
while chances>0:
    print("you have",chances,"chances left.")
    n = str(input("Enter your guess"))
    if num == n:
        print("Great! You got it right.")
        break
    else:
        for i in range(0,3):
            if n[i]==num[i]:
                bulls = bulls+1
            elif n[i] in num:
                cows = cows + 1
        print("Keep going. You have",bulls,"bulls and",cows,"cows.")
        bulls = 0
        cows = 0
        chances = chances - 1
print("The correct answer is",num)