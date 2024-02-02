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

def parseArguments(arguments, functions):
    return