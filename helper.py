def decoreer(tekst=""):
    tekst="header"
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()

def fooi_pp(bedrag, personen):
    bedrag_pp = bedrag/personen
    return f"Het bedrag per persoon is {bedrag_pp} euro."

def onderstreep(tekst=""):
    uit = []
    uit.append(tekst)
    uit.append(len(tekst) * "=")
    return uit

def som(inkomsten):
    totaal = 0
    for value in inkomsten:
        totaal += inkomsten[value]
    return totaal