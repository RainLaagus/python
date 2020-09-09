import random
print("Tere, mängime kivi, paber, käärid!")
valikud = ['kivi', 'paber', 'käärid']
mängija_valik = input("Tee enda valik: ")
if mängija_valik == valikud[0]:
    print("valisid kivi")
elif mängija_valik == valikud[1]:
    print("valisid paberi")
elif mängija_valik == valikud[2]:
    print("valisid käärid")
else:
    mängija_valik = input("See valik ei sobi, vali uuesti: ")

arvuti_valik = random.choice(valikud)
print("mina valisin " + arvuti_valik)

if mängija_valik == arvuti_valik:
    print("Jäime viiki")
elif mängija_valik == valikud[0] and arvuti_valik == valikud[1]:
    print("mina võitsin!")
elif mängija_valik == valikud[1] and arvuti_valik == valikud[2]:
    print("mina võitsin!")
elif mängija_valik == valikud[0] and arvuti_valik == valikud[2]:
    print("sina võitsid!")
elif mängija_valik == valikud[1] and arvuti_valik == valikud[0]:
    print("sina võitsid!")
elif mängija_valik == valikud[2] and arvuti_valik == valikud[1]:
    print("sina võitsid!")
else: 
    print("mina võitsin!")