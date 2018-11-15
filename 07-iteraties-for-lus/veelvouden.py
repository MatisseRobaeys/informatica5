#input
getal = int(input('getal?: '))

#denkwerk
som_veelvouden = 0
#rekenwerk
for i in range (0,101,getal) :
    som_veelvouden += i

print(som_veelvouden)