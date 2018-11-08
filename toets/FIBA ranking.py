#invoer
score_thuis = float(input('aantal punten thuisploeg: '))
score_uit = float(input('aantal punten uitploeg: '))
#berekening puntenverschil
puntenverschil_thuis_wint = float(score_thuis -score_uit)
puntenverschil_uit_wint = float(score_uit - score_thuis)
#berekening aantal ranking punten
if score_thuis > score_uit:
    if puntenverschil_thuis_wint >= 20:
        ranking_uit = float(270)
        ranking_thuis = float(730)
    elif puntenverschil_thuis_wint < 20 and puntenverschil_thuis_wint >= 10:
        ranking_thuis = float(630)
        ranking_uit = float(370)
    else:
        ranking_thuis = float(530)
        ranking_uit = float(470)
else:
    if puntenverschil_uit_wint >= 20:
        ranking_uit = float(870)
        ranking_thuis = float(130)
    elif puntenverschil_uit_wint < 20 and puntenverschil_uit_wint >= 10:
        ranking_uit = float(770)
        ranking_thuis = float(230)
    else:
        ranking_uit = float(670)
        ranking_thuis = float(330)
#uitvoer
lijn1 = '{}{:.2f}'.format('thuisploeg: ',ranking_thuis)
lijn2 = '  {}{:.2f}'.format('uitploeg: ',ranking_uit)

print(lijn1)
print(lijn2)
