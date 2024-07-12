def aanbieding_1(smaak, prijs, korting):
    tekst_1 = "Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak "
    tekst_2 = (f"{smaak}, van {prijs} euro voor {prijs - prijs * korting}")

    return tekst_1 + tekst_2

def inkomsten_totaal(inkomsten):
    for bedrag in inkomsten:
        bedrag = bedrag + bedrag
    return bedrag

# print(aanbieding_1("Aardbei", 4, 0.1))

# inkomsten = [220, 430, 125, 160, 205, 90, 345]

