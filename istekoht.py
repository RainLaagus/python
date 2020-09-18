from random import randint
a = input('Kas soovite istekoha ise valida? Kui jah siis kirjutage "ise" vastasel juhul kirjutage "loos": ')
c = randint(1,3)
if a == "ise":
    b = input('Kui soovite aknakohta sisestage "aken", kui soovite muud kohta sisestage "muu" ')
    if b == "aken":
        print("Valisite ise. Aknakoht")
    else:
        print("Valisite ise. Vahekäigukoht")
else:
    if c == 1:
        print("Istekoht loositi. Aknakoht")
    else:
        print("Istekoht loositi. Vahekäigukoht")