
def is_letter(n):
    q = ord('n')
    if n in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        mes = True

    else :
        mes = False
    return mes
def roteer_letter(a,b) :

    orda = ord(a)
    if orda > 65 and orda < 90 :
        if orda + b > 90 :
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
def versleutel(n):
