import random
kivi = "kivi"
paber = "paber"
käärid = "käärid"
valikud = [kivi, paber, käärid]
arvuti_valik = random.choice(valikud)

print("Tere, mängime kivi, paber, käärid!")

while True:
    mängija_valik = input("Tee enda valik: ")
    if mängija_valik in valikud: break
    print ("See valik ei sobi, vali uuesti: ")

if mängija_valik == paber:
    print("Sina valisid " + mängija_valik + "i.")
else:
    print("Sina valisid " + mängija_valik + ".")

if arvuti_valik == paber:
    print("Mina valisin " + arvuti_valik + "i.")
else:
    print("Mina valisin " + arvuti_valik + ".")

if mängija_valik == kivi and arvuti_valik == paber or mängija_valik == käärid and arvuti_valik == kivi or mängija_valik == paber and arvuti_valik == käärid:
    print("Mina võitsin!")
elif mängija_valik == kivi and arvuti_valik == käärid or mängija_valik == paber and arvuti_valik == kivi or mängija_valik == käärid and arvuti_valik == paber:
    print("Sina Võitsid!")
else: 
    print("Jäime viiki!")