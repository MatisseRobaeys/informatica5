#import
from math import sqrt
a = float(input('Geef een reel getal: '))
#denkwerk
if a == 2:
    mes = '2.00 is een nulpunt van f'
elif a > 2:
    beeld = sqrt(a - 2)
    mes = '{}{:.2f}{}{} {:.2f}'.format('f(',a ,')',' = ' ,beeld)
else:
    mes = 'a',' ∉ ', 'f(x)'

print(mes)
