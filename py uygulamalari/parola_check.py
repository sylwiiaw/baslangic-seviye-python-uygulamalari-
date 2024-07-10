
parola = input("Parolanizi girin: ")

if len(parola) < 8:
  print("Zayif: Parolaniz en az 8 karakter olmalidir.")
       
buyuk_harf = False
kucuk_harf = False
rakam = False
ozel_karakter = False
ozel_karakterler = "!@#$%^&*()-_+=<>?/"

for char in parola:
        if char.isupper(): #buyuk harfleri kontrol eder 
            buyuk_harf = True
        elif char.islower(): #kucuk harfleri kontrol eder 
            kucuk_harf = True
        elif char.isdigit(): #rakamlari kontrol eder 
            rakam = True
        elif char in ozel_karakterler: 
            ozel_karakter = True

if buyuk_harf and kucuk_harf and rakam and ozel_karakter:
 print( "Guçlu: Parolaniz guvenli.")
 
elif buyuk_harf and rakam:
 print ("Orta: Parolaniz daha guçlu olabilir.")
 
else:
    print ("Zayif:Parolaniz guvenli degil. Daha guclu olabilir")
 



