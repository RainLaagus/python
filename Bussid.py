inimeste_arv = input("Inimeste arv: ")
kohtade_arv = input("Kohtade arv: ")
täis_bussid = int(inimeste_arv) // int(kohtade_arv)
jääk = int(inimeste_arv) % int(kohtade_arv)

if jääk > 0:
    print("Busse vaja: " + str((täis_bussid)+1))
else:
    print("Busse vaja: " + str(täis_bussid))

if jääk == 0:
    print("Viimases bussis inimesi: " + kohtade_arv)
else:
    print("Viimases bussis inimesi: " + str(jääk))
# if jääk > 0:
#     print("Vaja läheb " + str((täis_bussid+1)) + " bussi ja viimases bussis on " + str(jääk) + " inimest.")
# else:
#     print("Vaja läheb " + str(täis_bussid) + " bussi ja kõik kohad on täis.")
