from math import  pi
ümbermõõt = float(input("Palun sisesta puu ümbermõõt sentimeetrites ja vajuta ENTER: "))
läbimõõt = (ümbermõõt / pi)
läbimõõt_a = round(läbimõõt, 2)
print("Antud puu läbimõõt on " + str(läbimõõt_a) + " cm.")
