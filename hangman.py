import random
import time


class User:
    def __init__(self, lives, score, time, nickname):
        self.lives = lives
        self.score = score
        self.constructTime = time
        self.nickname = nickname

    def user_input(self):
        return (input(f"Choose letter {self.nickname}: ")).lower()


def get_indexes(word):
    return [i for i in range(0, len(word)) if userInput == word[i]]


words = ("Book", "Handmade", "Bionicle", "Bathroom", "hate", "love", "mindful")

user = User(3, 100, time.time(), "shin")
# get random word from list
chosenWord = list((words[random.randint(0, len(words) - 1)]).lower())
hiddenWord = list("_" * len(chosenWord))

print(chosenWord)
while "_" in hiddenWord and user.lives > 0 and user.score > 0:
    userInput = user.user_input()
    if userInput in chosenWord:
        indexes = get_indexes(chosenWord)

        for i in indexes:
            user.score += 20
            hiddenWord[i] = userInput
        print("".join(hiddenWord))
    elif len(userInput) > 0 and userInput not in chosenWord:
        user.score -= 20
        user.lives -= 1
else:
    if user.score > 0 and user.lives > 0:
        print(f"user wins with score: {user.score} and {user.lives} lives")
    else:
        print(f"{user.nickname} lost")
