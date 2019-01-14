def is_palindroom (woord):
    a = -1
    q = 0
    omgekeerd_woord = woord[::-1]

    for letter in woord :
        a += 1
        if woord[a] == letter :
            q += 1
        else :
            return False
    return True



