from random import randint
kaart = int(input('kaart: '))
som_kaarten = 0

while som_kaarten + kaart < 21 and kaart > 0 :
    som_kaarten += kaart
    kaart = int(input('kaart: '))

if som_kaarten + kaart == 21:
    uivoer = 'Gewonnen!'
elif som_kaarten + kaart  < 21:
    uitvoer ='Voorzichtig gespeeld ({})'.format(som_kaarten+kaart)
else :
    uitvoer= 'Verbrand ({})'.format(totaal + kaart)

print(uitvoer)


