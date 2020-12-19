import random
import time


def get_indexes(word):
    return [index for index in range(0, len(word)) if userInput == word[index]]


class User:
    def __init__(self, lives, score, nickname):
        self.lives = lives
        self.score = score
        print(int(time.time()))
        self.construct_time = time.time()
        self.nickname = nickname

    def user_input(self):
        return (input(f"Choose letter {self.nickname}: ")).lower()
    def time_passed(self, actual_time):
        print(int(actual_time), int(self.construct_time))
        return int(actual_time-self.construct_time)




words = ("Book", "Handmade", "Bionicle", "Bathroom", "hate", "love", "mindful")
default_points = 10000
user = User(3, default_points, "shin")
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
        user.lives -= 1
else:
    if user.score > 0 and user.lives > 0:
        print(f"user wins with score: {user.score - user.time_passed(time.time())} and {user.lives} lives")
    else:
        print(f"{user.nickname} lost")
