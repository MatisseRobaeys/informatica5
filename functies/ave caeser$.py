def is_letter(n):
    q = ord('n')
    if n in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        return True

    else :
        return False

def roteer_letter(a,b) :

    orda = ord(a)
    if orda > 64 and orda < 91 :
        if orda + b > 91 :
            hulp = orda + b - 90
            nieuw = 64 + hulp
        else :
            nieuw = orda + b
    else :
        if orda + b > 122:
            hulp = orda + b - 122
            nieuw = hulp + 96
        else :
            nieuw = orda + b


    return chr(nieuw)
def versleutel(n,p):
    zin = ''
    for letter in n :
         if is_letter(letter) == True:
            gecodeerde_letter = roteer_letter(letter, p)
            zin += gecodeerde_letter
         else :

            zin += letter
    return zin
print(versleutel('Caroline is stom',20))

