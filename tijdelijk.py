# Les 7 Huiswerk 1

#2
prijzen = {"aardbei" : "3",
           "vanille" : "4",
           "chocolade": "5"}

#3
aanbieding = float(prijzen["aardbei"]) * 0.8

#4
reclame_tekst = (f"Vandaag in de aanbieding: aardbei-ijs, 1 liter - slechts € {aanbieding}")
# print(reclame_tekst)

#5
decimaal = reclame_tekst.index("0")
reclame_tekst2 = reclame_tekst[:decimaal]
# print (reclame_tekst2)

#6
reclame_tekst3 = reclame_tekst2.upper()
# print (reclame_tekst3)

#7
reclame_tekst4 = reclame_tekst3.split(" ")
# print (reclame_tekst4)

#8
for el in reclame_tekst4:
    print (el)

#9
for el in reclame_tekst4:
    print (el.lower())

#10
for el in reclame_tekst4:
    count = len(el)
    if (int(count) >= 5):
        print(el.upper())
    else:
        print(el.lower())