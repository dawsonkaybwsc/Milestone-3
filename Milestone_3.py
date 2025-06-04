import time

print("hello")
feeling_are = input("how many continents are there?: ") 
if int(feeling_are) > 7:
    print("Wrong there are 7")
if int(feeling_are) < 7:
    print("Wrong there are 7")
if int(feeling_are) > 100:
    print("answer the question properly")
if int(feeling_are) == 7:
    time.sleep(2)
    print("you're right It is 7")
    time.sleep(2)
print("51, 56, 53, 59")
your_answer = input("how many countries are in africa?: ")
if int(your_answer) > 53:
    print("you're wrong, it is 53, try again")
if int(your_answer) < 53:
    print("you're wrong, it is 53, try again")
if int(your_answer) > 100:
    print("answer the question properly")
if int(your_answer) == 53:
    time.sleep(2)
    print("you're right! It is 53")
time.sleep(3)
print("next question")
time.sleep(2)
name = input("How many great lakes are there?: ")
if int(name) > 5:
    print("you're wrong, it is 5, try again")
if int(name) < 5:
    print("you're wrong, it is 5, try again")
if int(name) > 100:
    print("answer the question properly")
if int(name) == 5:
    time.sleep(2)
    print("you're right! it is 5")
age = input("Your age: ")
time.sleep(2)
print("your age is", age,)
