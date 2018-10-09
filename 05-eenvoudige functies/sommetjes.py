a =float( input('a : '))
b = float(input('b: '))

#berekening
resultaat_1= '{:.0f} + {:.0f} = {:.0f}'.format(a, b, a+b)
resultaat_2= '{:.0f} + {:.0f} = {:.0f}'.format(a*(10**1),b*(10**1),a*(10**1)+ b*(10**1))
resultaat_3= '{:.0f} + {:.0f} = {:.0f}'.format(a*(10**2),b*(10**2),a*(10**2)+ b*(10**2))
resultaat_4= '{:.0f} + {:.0f} = {:.0f}'.format(a*(10**3),b*(10**3),a*(10**3)+ b*(10**3))
resultaat_5= '{:.0f} + {:.0f} = {:.0f}'.format(a*(10**4),b*(10**4),a*(10**4)+ b*(10**4))



#output
print(resultaat_1)
print(resultaat_2)
print(resultaat_3)
print(resultaat_4)
print(resultaat_5)
