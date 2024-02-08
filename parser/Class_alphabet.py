class Alphabet: #this is used to tell the parser what to do with what strings/characters
    seperators = [" ", ",", ":", ".", "-"] #basic seperators would include [" ",",",":",".","-"]
    returners = [";", "#"] #these are used for comments, after it is read everything else is ignored
    arguments = [] #these would be entire words which are matched against to call functions
    def __init__(self, seperators, returners, arguments) -> None:
        self.seperators = seperators
        self.returners = returners
        self.arguments = arguments
        