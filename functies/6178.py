def splits (a) :
    getal = a
    duizendtal = getal // 1000
    hondertal  = (getal // 100) - (duizendtal*10)
    tiental = (getal // 10) - ((duizendtal*100)+(hondertal*10))
    eenheid = (getal)- ((duizendtal*1000)+(hondertal*100)+(tiental*10))

    return duizendtal, hondertal, tiental, eenheid

def oplopende_cijfers (a, b, c, d):
    s1 = min(a, b, c, d)
    s4 = max(a, b, c, d)
    #middenste getallen bepalen
    k23 = max(min(a, b), min(b, c),min(a, c))
    k32 = a + b + c + d - s1 - s4 - k23
    #middenste getallen in volgorde plaatsen
    s2 = min(k23, k32)
    s3 = max (k23, k32)

    return (s1, s2, s3, s4)

def op_af_getellen (a, b, c, d):
    return str(a)+str(b)+ str(c) + str(d), str(d) + str(c)+ str(b) + str(a)

def verschil(af, op) :
    uitkomst = str(int(af )- int(opl))
    while len(uitkomst) < 4 :
        uitkomst = '0' + uitkomst
    return uitkomst
def kaprekar (getal):
    while getal != 6174 :
        a, b, c, d = splits(getal)
        w, x, y, z = oplopende_cijfers(a, b, c, d)
        op, af = oplopende_cijfers(w, x, y, z)
        v = verschil(af, op)
        getal = int(v)
        uitkomst += af + ' - ' + op + ' = ' + v
        if getal != 6174:
            uitkomst += '\n'
    return  uitkomst