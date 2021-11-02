def naamEnLeeftijd(name):
    print("Je kan op elk moment stoppen door stop in te voeren bij 1 van de 2 vragen.")
    voornaam = input("Wat is je voornaam?: ").lower()
    if voornaam == "stop":
        return voornaam
    leeftijd = input("Wat is je leeftijd?: ").lower()
    if leeftijd == "stop":
        return leeftijd
    print("Hallo " + voornaam + ", je leeftijd is " + leeftijd + " jaar")

while True:
    if naamEnLeeftijd("name") == "stop":
        break
    naamEnLeeftijd("name")