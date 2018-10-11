a = float(input('geef lengte a: '))
b = float(input('geef lengte b: '))
c = 'schuine zijde'

from math import sqrt as vierkantswortel

linker_lid= vierkantswortel((a**2) + (b**2))
rechter_lid= c

print('{} {} {:.2f} {} {} {:.2f} {} {:.2f}'.format('in een rechthoekige driehoek met rechthoekszijden','a=',a,'en','b=',b,'is de schuine zijde',linker_lid))
