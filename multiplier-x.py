def vraagTafel(antwoordTafel: int):
    antwoordTafel = int(input("Voor welk getal wilt u de tafel zien? (1 t/m 10): "))
    
    for i in range(1, 11):
        answer = antwoordTafel * i
        print(antwoordTafel, 'x', i, '=', answer)

vraagTafel("antwoordTafel")