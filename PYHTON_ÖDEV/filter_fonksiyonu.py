liste = [(3,4,5),(6,8,10),(3,10,7)]

def ucgenMi(demet):
    if abs(demet[0]+demet[1]) > demet[2] and (demet[0]+demet[2]) > demet[1] and (demet[0]+demet[2]) > demet[1]:
        return True
    else:
        return False
    
liste2 = list(filter(ucgenMi, liste))

print(liste2)