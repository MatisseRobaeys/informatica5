#input
sv = float(input('snelheid vrachtwagens?: '))
dv = float(input('dichtheid vrrachtwagens?: '))
sa = float(input('snelheid auto?: '))
da = float(input('dichtheid auto?: '))
#berekening kans op file
fv = min((sv * dv)/ 40 , 1)
fa = min((sv * dv)/ 40 , 1)
fmin = float(min(fv,fa))
fmax = float(max(fv,fa))
fverschil = abs(float(fv - fa))

#berekenen kleurcode
if fmin > 0.7 :
    mes = 'zwart'
elif fmax > 0.7 and (fverschil < 0.2) :
    mes ='rood'
elif fverschil > 0.7 :
    mes = 'geel'
else:
    mes = 'groen'
#uitvoer
print(mes)