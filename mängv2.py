import random
kivi = "kivi"
paber = "paber"
käärid = "käärid"
valikud = [kivi, paber, käärid]
arvuti_valik = random.choice(valikud)

def ilusta_valik(valik):
    if valik == paber:
        return valik + "i."
    else:
        return valik + "."

print("Tere, mängime kivi, paber, käärid!")

mängija_valik = input("Tee enda valik: ")
while not mängija_valik in valikud:
    print ("See valik ei sobi, vali uuesti: ")
    mängija_valik = input("Tee enda valik: ")
print("Sina valisid " + ilusta_valik(mängija_valik))
print("Mina valisin " + ilusta_valik(arvuti_valik))


if ((mängija_valik == kivi and arvuti_valik == paber) or
    (mängija_valik == käärid and arvuti_valik == kivi) or
    (mängija_valik == paber and arvuti_valik == käärid)):
    print("Mina võitsin!")
elif ((mängija_valik == kivi and arvuti_valik == käärid) or
    (mängija_valik == paber and arvuti_valik == kivi) or
    (mängija_valik == käärid and arvuti_valik == paber)):
    print("Sina Võitsid!")
else: 
    print("Jäime viiki!")