hendel_trekken = input('trek aan de hendel van de wissel? (ja/nee): ')

if hendel_trekken == 'ja':
    man_doden = input('duw je de man van de brug?(ja/nee): ')
    if man_doden== 'ja':
        doden=2
    else:
        doden = 1
else:
    man_doden = input('duw je de man van de brug ? (ja/nee): ')
    if man_doden == 'ja':
        doden = 1
    else:
        doden = 5
print(doden)