ilkSayi = float(input("ilk sayiyi giriniz: "))
ikinciSayi= float(input("ikinci sayiyi giriniz: "))
islem = input("Yapmak istediginiz islemi seciniz(+,-,*,/): ")

if islem == "+":
  print("sonuc = " + str(ilkSayi+ikinciSayi))

elif islem == "-":
  print("sonuc = " + str(ilkSayi-ikinciSayi))

elif islem == "*":
  print("sonuc = " + str(ilkSayi*ikinciSayi))

elif islem == "/":
  print("sonuc = " + str(ilkSayi/ikinciSayi))

else:
  print("Gecersiz islem! Islem seciniz lutfen...")
