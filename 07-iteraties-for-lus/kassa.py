prijs = int(input('prijs?: '))
totaal = 0
while prijs != 0 :
    totaal += prijs
    prijs = float(input('prijs?: '))

uitput = 'De totale prijs is € {:.2f}'.format(totaal)
print(uitput)