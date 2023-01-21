print("welcome to my computer quiz!")   #game 1: Computer quiz.

playing = input ("do you want to play?")
if playing != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("what does GPU stand for? ")
if answer == "graphics processing unit":
    print('correct!')
    score += 1
else:
    print("Sorry, but that is incorrect")

answer = input("what does RAM stand for? ")
if answer == "random access memory":
    print('correct!')
    score += 1
else:
    print("Sorry, but that is incorrect")

awnser = input("what does PSU stand for? ")
if answer == "power supply unit":
    print('correct!')
    score += 1
else:
    print("Sorry, but that is incorrect")


print("you got " + str(score) + " questons correct! ")
print("you got " + str((score / 3) * 100) + "%.")

