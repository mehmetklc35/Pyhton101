with open("futbolcular.txt","r",encoding="utf-8") as file1:
    for satir in file1:
        satir = satir[:-1]
        satir_elemanlari = satir.split(",")
        
        if satir_elemanlari[1] == "Galatasaray":
            with open("gs.txt","a",encoding="utf-8") as file2:
                file2.writelines(satir_elemanlari[0])+"\n"
                
        elif satir_elemanlari[1] == "Fenerbahçe":
            with open("fb.txt","a",encoding="utf-8") as file3:
                file3.writelines(satir_elemanlari[0])+"\n"
                
        else:
            with open("bjk.txt","a",encoding="utf-8") as file4:
                file4.writelines(satir_elemanlari[0])+"\n"