
# Some applications keep all their strings in a common resource in order to save memory by avoiding duplicate strings.
# Take string input from the user in a loop. 
# First take the string tag (user input defined "value" for dict), then the string value. 
# Each string is stored in a dictionary. 
# If an input of a string is already in the dictionary, don’t add it but give an error saying it already exists and show what tag it has. 
# If the tag is the same then change the string value of that tag. At the end, print out the string list.

# If string is same, don't add. (key)
# If tag is same, add/update. (value)

class Flywieght:
    _StringDict = {}
 
    @classmethod
    def add_to_dict(cls):
        tag = input("Enter a tag for the string: ")
        string = input("Enter a string: ")
        if string in cls._StringDict:
            print(f"Error: String already exists with tag '{cls._StringDict[string]}'.")
        elif tag == cls._StringDict[string]:
            # Ask about this

            return

    @classmethod
    def show_string_dict(cls):
        for string in cls._StringDict:
            key = string
            val = cls._StringDict[key]
            print(f"{key}: {val}")

