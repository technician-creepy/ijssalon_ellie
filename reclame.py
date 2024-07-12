from algemene_functies import mijn_functie2

def aanbieding_1(smaak, prijs, korting):
    tekst_1 = "Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak "
    tekst_2 = (f"{smaak}, van {prijs} euro voor {prijs - prijs * korting}")

    return tekst_1 + tekst_2

def inkomsten_totaal(inkomsten, btw):
    totaal = 0
    for bedrag in inkomsten:
        totaal = totaal + bedrag
    
    btw = totaal * btw
    totale_inkomsten = (f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw} euro btw betaald dient te worden.")
    return totale_inkomsten

def laag_en_hoog(mijn_lijst):
    hoogste = max(mijn_lijst)
    laagste = min(mijn_lijst)
    return [hoogste, laagste]

def gemiddelde(mijn_lijst):
    totaal = 0
    for inkomst in mijn_lijst:
        totaal = totaal + inkomst
    week_gemiddelde = totaal / 7
    gemiddeld = (f"De gemiddelde inkomsten deze week zijn {week_gemiddelde} euro")
    return gemiddeld

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie2(korte_lijst[0],korte_lijst[1])
    return uitvoer