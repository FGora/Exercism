def is_isogram(string):
    letters=[letter.lower() for letter in string if letter.lower() in "abcdefghijklmnopqrstuvwxyz"]
    for letter in letters:
        letters.remove(letter)
        if letter in letters:
            return False
    return True        
