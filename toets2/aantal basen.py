#invoer
aantal_basen = int(input('aantal basen?: '))
verschillende_basen = ''
aantal_verschillende_basen = 0


#uitvoeren + denkwerk
for i in range (aantal_basen):
    base = str(input('base?: '))
    if base not in verschillende_basen :
        verschillende_basen += base + ' '
        aantal_verschillende_basen += 1

#antwoord
if aantal_verschillende_basen == 1:
    print('De DNA-keting bevat 1 soort base: {} '.format(verschillende_basen))
elif aantal_verschillende_basen > 1 :
    print('De DNA-keting bevat {} verschillende soorten basen:{}'.format(aantal_verschillende_basen,verschillende_basen))



