def hint(gok, woord):
#woord en gok splitsen
    geraden  = ''
    eerste_letter_g = gok[0]
    tweede_letter_g = gok[1]
    derde_letter_g = gok[2]
    vierde_letter_g = gok[3]
    vijfde_letter_g = gok[4]

    eerste_letter_w = woord[0]
    tweede_letter_w = woord[1]
    derde_letter_w = woord[2]
    vierde_letter_w = woord[3]
    vijfde_letter_w = woord[4]


    if eerste_letter_g in woord and eerste_letter_g == eerste_letter_w:
        geraden  += eerste_letter_g.upper()
    elif eerste_letter_g in woord:
        geraden += eerste_letter_g
    else:
        geraden += '.'
    if tweede_letter_g in woord and tweede_letter_g == tweede_letter_w:
        geraden += tweede_letter_g.upper()
    elif tweede_letter_g in woord:
        geraden += tweede_letter_g
    else:
        geraden += '.'
    if derde_letter_g in woord and derde_letter_g == derde_letter_w:
        geraden += derde_letter_g.upper()
    elif derde_letter_g in woord:
        geraden += derde_letter_g
    else:
        geraden += '.'
    if vierde_letter_g in woord and vierde_letter_g == vierde_letter_w:
        geraden += vierde_letter_g.upper()
    elif vierde_letter_g in woord:
        geraden += vierde_letter_g
    else:
        geraden += '.'
    if vijfde_letter_g in woord and vijfde_letter_g == vijfde_letter_w:
        geraden += vijfde_letter_g.upper()
    elif vijfde_letter_g in woord:
        geraden += vijfde_letter_g
    else:
        geraden += '.'

    return geraden