print ("""
        Latihan Dictionary
        Nama : Reinalddy 
        Nim :312110522
    
""")


kontak = { 'kontak1' : 'Ari',
           'NoHpAndi' : '6281267888',
           'kontak2' : 'dina',
           'NoHpDina' : '627677776' 
           }

kontak['kontak3'] = 'Riko'
kontak['NoHpriko'] = '087654544'
kontak['NoHpDina'] = '088999776'
del kontak ['kontak2']
del kontak ['NoHpDina']

print("._____________________________________.")
print("|             Contact          |")
print("|_____________________________________|")
print("| Nama    |      No           | ")
print (kontak ['kontak1'],"        ",kontak ['NoHpAndi'])
#print (kontak ['kontak2'],"        ",kontak['NoHpDina'])
print (kontak ['kontak3'],"        ",kontak['NoHpriko'])









