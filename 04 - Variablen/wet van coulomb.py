k = float(8.99 * (10**9))
q_een = float(2.0 *(10**-6))
q_twee = float(1.0*(10**-6))

r = float(input('afstand: '))

resultaat = (q_twee * q_een)
resultaat /= (r*(10**-2))**2

resultaat *= k

print(resultaat)
