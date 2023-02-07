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

print("welcome to part 2 of my computer game!")              #pt 2 of my computer quiz
playing = input ("do you want to play?")
if playing != "yes":
    quit()

print("great!")
print("in this part, we are going to guess games!")


print("Okay! Let's play :)")
score = 0

answer = input("what game do children play very often now? ")
if answer == "roblox":
    print('correct!')
    score += 1
else:
    print("Sorry, but that is incorrect")

answer = input(" what game has zerg, protoss, and terrain races? *hint: it's on battle.net! ")
if answer == "Starcraft":
    print('correct!')
    score += 1
else:
    print("Sorry, but that is incorrect")

answer = input(" what game was called cave game in 2009, but has a different name now? ")
if answer == "minecraft":
    print('correct!')
    score += 1
else:
    print("Sorry, but that is incorrect")

answer = input(" is there a world of starcraft? ")
if answer == " no ":
    print('correct!')
    score += 1
else:
    print("Sorry, but that is incorrect")

    print("you got " + str(score) + " questons correct! ")

averageScore = (score / 4) * 100
print("you got " + str(averageScore) + "%")

if averageScore >= 0:
    print("           O O           ")
    print("            ====)           ")
    print("         \______/      ")
