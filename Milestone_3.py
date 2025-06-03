import time

print("hello")
feeling_are = input("how many continents are there? ") 
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
print("how many countries are in africa?")
print("51, 56, 53, 59")
your_answer = input("Answer: ")
print("your guess was", your_answer)
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
print("what is your name?")
name = input("Your name: ")
time.sleep(2)
print("okay, what is your age")
age = input("Your age: ")
time.sleep(2)
print("okay so your name is", name, "your age is", age,)
