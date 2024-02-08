import Class_alphabet

class CustomException(Exception):
    def __init__(self, message):
        super().__init__(message)

class Parser:
    def __init__(self, alphabet) -> None:
        self.alphabet = alphabet 

    def parsemMessage(string, alphabet):
        current = ""
        argumentList = []
        charList = []
        for char in string:
            charList.append(char)
        for char in charList:
            if char in alphabet.returners: 
                return argumentList
            if char in alphabet.seperators: 
                argumentList.append(current)
                current = ""
            else: 
                current.append(char)
        return argumentList

    def parseArguments(arguments, alphabet):
        for argument in arguments:
            if argument not in alphabet:
                raise CustomException("Invalid Argument")
            
            