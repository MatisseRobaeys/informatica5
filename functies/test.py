def volgend_collatz_getal(n) :
    if n % 2 == 0:
        volgendgetal =  n // 2
    else :
        volgendgetal = n * 3 + 1
    return volgendgetal


def collatz(n) :
    i = 1
    volgend_getal = volgend_collatz_getal(n)
    while n != 1  :
        i += 1
        n = volgend_getal
        volgend_getal = volgend_collatz_getal(n)

    return i

