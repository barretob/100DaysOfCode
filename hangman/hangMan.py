
import random
import hangmanArt
import hangmanWords


lives = 6

print(hangmanArt.logo)

randomWord = random.choice(hangmanWords.word_list)
print(randomWord)

display = []

for letter in randomWord:
    display.append("_")

endOfGame = False
while not endOfGame:

    userInput = input("Guess a letter:").lower()

    if userInput in display:
        print(f"You have already guess {userInput}")

    for i in range(0, len(display)):
        if userInput == randomWord[i]:
            display[i] = userInput

    print(f"{' '.join(display)}")

    if "_" not in display:
        endOfGame = True
        print("did it work?")

    if userInput not in randomWord:
        lives = lives - 1
        print(f"The letter {userInput} is not in the word. You lose a life!")

    print(hangmanArt.stages[lives])

    if lives == 0:
        print("You lose!")
        endOfGame = True
