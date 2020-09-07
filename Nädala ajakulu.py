ainepunktide_arv = int(input("Sisesta ainepunktide arv täisarvuna: "))
nädalate_arv = int(input("Sisesta nädalate arv täisarvuna: "))
nädala_ajakulu = ainepunktide_arv * 26 / nädalate_arv
print(round(nädala_ajakulu))