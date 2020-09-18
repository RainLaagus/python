vanus = int(input("Sisestage enda vanus: "))
sugu = input("Sisestage enda sugu (M või N): ").lower()
treeningu_tüüp = input("Sisestage treeningu tüüp (1 - tervisetreening, 2 - põhivastupidavuse treening, 3 - intensiivne aeroobne treening): ")

if sugu == "m" and treeningu_tüüp == "1":
    print("Pulsisagedus peaks olema vahemikus " + str(round((220 - vanus) * 0.5)) + " kuni " + str(round((220 - vanus) * 0.7)))
elif sugu == "m" and treeningu_tüüp == "2":
    print("Pulsisagedus peaks olema vahemikus " + str(round((220 - vanus) * 0.7)) + " kuni " + str(round((220 - vanus) * 0.8)))
elif sugu == "m" and treeningu_tüüp == "3":
    print("Pulsisagedus peaks olema vahemikus " + str(round((220 - vanus) * 0.8)) + " kuni " + str(round((220 - vanus) * 0.87)))
elif sugu == "n" and treeningu_tüüp == "1":
    print("Pulsisagedus peaks olema vahemikus " + str(round((206 - (vanus * 0.88)) * 0.5)) + " kuni " + str(round(((206 - (vanus * 0.88)) * 0.7))))
elif sugu == "n" and treeningu_tüüp == "2":
    print("Pulsisagedus peaks olema vahemikus " + str(round((206 - (vanus * 0.88)) * 0.7)) + " kuni " + str(round(((206 - (vanus * 0.88)) * 0.8))))
else:
    print("Pulsisagedus peaks olema vahemikus " + str(round((206 - (vanus * 0.88)) * 0.8)) + " kuni " + str(round(((206 - (vanus * 0.88)) * 0.87))))