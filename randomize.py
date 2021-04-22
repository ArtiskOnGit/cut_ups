# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from random import choice


def randomize(text, *texts):
    returned = []
    #print(texts)
    if not texts:
        texts = ""
    else:
        texts = "".join([el for el in texts])
    all_text = (text + texts).split(" ")
    while len(all_text) != 0:
        word = choice(all_text)
        returned.append(word)
        all_text.remove(word)
    return " ".join(returned)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    randomize('PyCharm')
    print(randomize('Press the green button in the gutter to run the script', "Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
