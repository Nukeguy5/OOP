
from abc import ABC, abstractmethod

class Language(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def message(self):
        pass


class English(Language):
    def message(self):
        name = input("Enter your name: ")
        print("Hello " + name + "!")


class PigLatin(Language):
    def message(self):
        name = input("Enteryay ouryay amenay: ")
        print("Ellohay " + name + "!")


if __name__ == "__main__":
    while True:
        language = input("Type English, Pig Latin, or quit: ")
        if language.lower() == "english":
            English().message()
        elif language.lower() == "pig latin":
            PigLatin().message()
        elif language.lower() == "quit":
            break
        else:
            print("Please enter English, Pig Latin, or quit.")      
