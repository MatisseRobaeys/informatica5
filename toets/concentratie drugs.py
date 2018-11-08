#import
import math
#invoer
tijd = float(input("tijd in uren: "))

#berekening concentratie
teller = float(math.pi * tijd)
noemer = float(tijd **2 + 2)
concentratie = float(teller / noemer)

#uitvoer
mes = '{:.4f}'.format(concentratie)

print(mes)

