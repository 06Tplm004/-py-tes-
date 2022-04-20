nim=int(input("191011400504 ="))
nama=str(input(" Edi Kurniawan ="))
mata_kuliah=str(input(" Kecerdasan Buatan ="))
nilai_absensi=int(input("14 ="))
nilai_tugas=int(input("80 ="))
nilai_uts=int(input("85 ="))
nilai_uas=int(input(" 75 ="))
 
print("============================================================")
print("\n","NIM = ",nim,"\n","NAMA = ",nama,"\n","MATA KULIAH = ",mata_kuliah)
a=nilai_absensi*20/100
b=nilai_tugas*25/100
c=nilai_uts*25/100
d=nilai_uas*30/100
nilai_akhir=a+b+c+d
print("\n","NILAI AKHIR =",nilai_akhir)
if nilai_akhir >=81:
    print("\n","GRADE A")
elif nilai_akhir >= 75:
    print("\n","GRADE B")
elif nilai_akhir >= 60:
    print("\n","GRADE C")
elif nilai_akhir >= 41:
    print("\n","GRADE D")
else :
    print("\n","GRADE E")
print("============================================================")
