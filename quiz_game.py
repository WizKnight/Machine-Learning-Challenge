print("Welcome To The Valorant Game Quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
    
print("Okay! Let's playyyy :)")
score = 0

answer = input("Q1. How many Rounds are needed to win the game? ")
if answer == "13":
    print("Correct!")
    score += 1
else:
    print(f"The answer is '13', not {answer!r}")
    
answer = input("Q2. Which Agent says,We have one job. Save the Earth. No Excuses.? ")
if answer.lower() == "neon":
    print("Correct!")
    score += 1
else:
    print(f"The answer is 'neon', not {answer!r}")
    
answer = input("Q3. Who is the oldest Valorant agent? ")
if answer.lower() == "brimstone":
    print("Correct!")
    score += 1
else:
    print(f"The answer is 'brimstone', not {answer!r}")
    
answer = input("Q4. What is the minimum age to play Valorant? ")
if answer == "18":
    print("Correct!")
    score += 1
else:
    print(f"The answer is '18', not {answer!r}")
    
answer = input("Q5. Which country is KillJoy from? ")
if answer.lower() == "germany":
    print("Correct!")
    score += 1
else:
    print(f"The answer is 'germany', not {answer!r}")
    
print("You got " + str(score) + " questions correct!")
print("You got " + str((score/5) * 100) + "%.")
    
