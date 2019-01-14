prijzengeld = 0
woord = input('woord?: ')
geld = float(input('gedraaid: '))
letter = input('letter?: ')
raden = ''
while (letter in woord) and (letter not in raden):
    prijzengeld += geld

    raden += letter
    letter = input('letter?: ')

print(prijzengeld)