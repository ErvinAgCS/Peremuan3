Nilai_a = int(input("Masukan Nilai MTK :"))
Nilai_b = int(input("Masukan Nilai English :"))
Nilai_c = int(input("Masukan Nilai Algoritma :"))

Jumlah = Nilai_a + Nilai_b + Nilai_c

if Jumlah > 80 :
    print ("A")
elif Jumlah > 70 :
    print ("B")
elif Jumlah > 60 :
    print ("C")
elif Jumlah > 50 :
    print ("D")
else :
    print ("E")
    