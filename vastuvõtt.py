punkti_summa = float(input("Palun sisesta enda punktisumma: "))
if punkti_summa < 66 and punkti_summa >= 0:
    print("Vähem kui kandideerimiseks vajalik")
elif punkti_summa >= 66 and punkti_summa < 85:
    print("Kandideerimine vastuvõtule")
elif punkti_summa >= 85 and punkti_summa <= 100:
    print("Vastuvõtt tagatud")
else:
    print("Vigane punktisumma")