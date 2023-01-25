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

answer = input("what does PSU stand for? ")
if answer == "power supply unit":
    print('correct!')
    score += 1
else:
    print("Sorry, but that is incorrect")

answer = input("What sports does your dad play? ")
if answer == "basketball":
    print('Correct!')
    score += 1
else:
    print("Go ask your dad again!")

print("you got " + str(score) + " questons correct! ")

averageScore = (score / 4) * 100
print("you got " + str(averageScore) + "%")

if averageScore >= 0:
    print("           O O           ")
    print("            ====)           ")
    print("         \______/      ")

