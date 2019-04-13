
# Some applications keep all their strings in a common resource in order to save memory by avoiding duplicate strings.
# Take string input from the user in a loop. 
# First take the string tag (user input defined "value" for dict), then the string value. 
# Each string is stored in a dictionary. 
# If an input of a string is already in the dictionary, don’t add it but give an error saying it already exists and show what tag it has. 
# If the tag is the same then change the string value of that tag. At the end, print out the string list.

# If string is same, don't add. (value)
# If tag is same, add/update. (tag)

class Flywieght:
    _StringDict = {}
 
    @classmethod
    def update_dict(cls, tag, string):
        for k, v in cls._StringDict.items():
            if string == v:
                print(f"ERROR: String '{string} already exists with tag '{k}'.")
                return
        cls._StringDict[tag] = string

    @classmethod
    def print_strings(cls):
        print('-'*6, "Final", '-'*6)
        for key, val in cls._StringDict.items():
            print(f"{key} => {val}")
        print('-'*19)

def main():
    while True:
        tag = input("Enter a tag (or /q to quit): ")
        if tag == "/q":
            break
        string = input("Enter a string: ")
        Flywieght.update_dict(tag, string)
    Flywieght.print_strings()
    Flywieght._StringDict.clear()

if __name__ == "__main__":
    main()
