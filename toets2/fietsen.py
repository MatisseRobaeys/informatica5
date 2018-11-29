#invoer
snelheid_stijn = int(input('snelheid stijn?: '))
snelheid_kaat = int(input('snelheid kaat?: '))
afstand = int(input('afstand?: '))

#denkwerk
tijd = 1
afstand_stijn = snelheid_stijn * tijd
afstand_kaat = snelheid_kaat * tijd
#uitvoeren
while afstand_stijn + afstand_kaat <= afstand :
    tijd += 1
    afstand_stijn = snelheid_stijn * tijd
    afstand_kaat = snelheid_kaat * tijd

#antwoord
print('Na {} s hebben Stijn en Kaat elkaar ontmoet.'.format(tijd))
