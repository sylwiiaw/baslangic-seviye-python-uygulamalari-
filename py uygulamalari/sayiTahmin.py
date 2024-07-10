import random

    
rastgele_sayi = random.randint(1, 100)
    
print("1-100e kadar olan bir sayiyi tahmin et.10 takim etme hakkin var")

tahmin_hakki = 10
    
while tahmin_hakki > 0:
        tahmin = int(input("Tahmininizi girin: "))
        
        if tahmin < rastgele_sayi:
            print("Daha yüksek bir sayi tahmin edin.")
        elif tahmin > rastgele_sayi:
            print("Daha düşük bir sayi tahmin edin.")
        else:
            print("Tebrikler!Doğru tahmin ettiniz.")
            break
        
        tahmin_hakki -= 1
        print(f"Kalan tahmin hakkiniz: {tahmin_hakki}")
        
if tahmin_hakki == 0:
        print(f"Üzgünüm, tahmin hakkiniz bitti. Doğru sayi {rastgele_sayi} idi.")









