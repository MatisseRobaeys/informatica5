#invoer

speler_een = input('gebaar speler een?: ')
speler_twee = input('gebaar speler twee?: ')

#winnaar beslissen

if speler_een == 'blad' and speler_twee == 'steen':
    uitvoer = 'speler 1 wint'
elif speler_een == 'schaar' and speler_twee == 'blad':
    uitvoer = 'speler 1 wint'
elif speler_een == 'steen' and speler_twee == 'schaar':
    uitvoer = 'speler 1 wint'
elif speler_een == speler_twee:
    uitvoer = 'onbeslist'
else :
    uitvoer = 'speler 2 wint'
print(uitvoer)


