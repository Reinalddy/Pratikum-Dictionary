

print (""" 
        Program Input Nilai
        ===================
          """)
z = 0   






while z < 100 :
    z+=1
    Cmd = input ("(L)ihat , (T)ambah , (U)Ubah , (H)apus , C(ari) (K)eluar : ")

    if Cmd == "T" :
        print ("tambah data")
        Nama = {'nama': input ("masukan nama :")}
        Nim = {'nim' : input ('masukan Nim : ') }
        Tugas = {'tugas' : input ('masukan Nilai Tugas : ') }
        Uts = {'uts' : input ('Masukan Nilai Uts :')}
        Uas = {'uas': input ('masukan NIlai Uas :') }
    
    elif Cmd == "L" :
        break

    elif Cmd =="H":
        del  Nama

    elif Cmd == "U":
        print ("ubah data")
        Nama = {'nama': input ("masukan nama yang di ubah : ")}
        Nim = {'nim' : input ('masukan Nim yang di ubah : ') }
        Tugas = {'tugas' : input ('masukan Nilai Tugas yang di ubah : ') }
        Uts = {'uts' : input ('Masukan Nilai Uts yang di ubah :')}
        Uas = {'uas': input ('masukan NIlai Uas yang di ubah :') }

    elif Cmd ==  "C" :
        print ("cari data")
        a = input ("data apa yang ingin di cari ? (nama,nim,tugas,uts,uas")
        if a == "nama" :
            print (Nama)    
        elif a == "nim" :
            print (Nim)
        elif a == "tugas" :
            print (Tugas)
        elif a == "uts" :
            print (Uts)
        elif a == "uas" :
            print (Uas) 
        else :
            print ("data yang kamu masukan tidak valid")


    elif Cmd == "K" :

        print ("kamu telah keluar dari program") 
        break                  

       
   


for z in range(z):
    print("| ",z+1,"   |  ",Nama,"  |  ",Nim,"    |      ",Tugas,"      |      ",Uts,"     |     ",Uas,"      |         |")
  
 

        




