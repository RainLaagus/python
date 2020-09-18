kirja_suurus = float(input("Sisestage kirja suurus: "))
pealkiri = input("Sisestage kirja teema pealkiri: ")
manus = input("Kas kirjaga on kaasas fail? ")

if (manus == "jah" and kirja_suurus > 1.0) or pealkiri == "":
    print("Kiri on spämm")
else:
    print("Kiri ei ole spämm")