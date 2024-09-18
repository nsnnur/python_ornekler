"""print("hello world")"""

#2
"""int(input("adınızı giriniz="))"""

#3
"""sayi1=int(input("1. sayıyı giriniz:"))
sayi2=int(input("2. sayıyı giriniz:"))
print(sayi1+sayi2)"""

#4
"""sayi1=int(input("1. sayıyı giriniz:"))
sayi2=int(input("2. sayıyı giriniz:"))
print(sayi1/sayi2)"""

#5
"""vize=int(input("vize notonuzu giriniz:"))
final=int(input("final notunuzu giriniz:"))
print((vize+final)/2)"""

#6
"""sayi1=int(input("1. notu giriniz:"))
sayi2=int(input("2. notu giriniz:"))
sayi=int(input("3. notu giriniz:"))
print((sayi1+sayi2+sayi3)/3)"""

#7
"""sayi1=int(input("ortalamanızı giriniz:"))
if(sayi1<50):
    print("Kaldın")
else:
    print("geçtiniz")"""

#8
"""sayi=int(input("sayı giriniz"))
if (sayi%2==0):
    print("çift")
else:
    print("tek")"""

#9
"""sayi=int(input("sayı giriniz"))
if (sayi<0):
    print("negatif sayı")
elif (sayi>0):
    print("çift sayı")
else:
   print("sıfır")"""

#10
"""boy=float(input("boy giriniz:"))
kilo=float(input("kilo giriniz:"))
vki=kilo/(boy*boy)
if(vki<18):
    print("zayıf")
elif(vki>25):
    print("obez")
else:
    print("normal")"""

#11
"""yas=int(input("yaşınızı giriniz:"))
if(yas<18)
    print("ehliyet alamaz")
else:
    print("ehliyet alabilir")"""
#12
"""for i in range(101):
    print(i)"""

#13
"""for i in range(101):
    if(i%2==0):
        print(i)"""

#14
"""for i in range(101):
    if(i%2==1):
        print(i)"""

#15
"""for i in range(101):
    if(i%3==0 and i%5==0):
        print(i)"""

#16
"""sayi1=int(input("bir sayı giriniz:"))
for i in range(sayi1):
       print(i)"""

#17
"""kisa=int(input("kısa kenar için bir sayı giriniz:"))
uzun=int(input("uzun kenar için bir sayı giriniz:"))
alan=kisa*uzun
print(alan)
cevre=2*(kisa+uzun)
print(cevre)"""

#18
"""kelime=input("bir metin girin:")
for harf in kelime:
    print(harf)"""

#19
"""sayi1=int(input("1. sayıyı giriniz:"))
sayi2=int(input("2. sayıyı giriniz:"))
toplam=0
for i in range(sayi1,sayi2+1):
   toplam==i
 print("sayıların toplamı: ".format(toplam))"""

#20
"""secim=input("sinema için(1), tiyatro için(2)")
ogrenci= input("öğrenci misiniz(e/h)")
ucret=0
if secim== '1':
    ucret=15
elif secim == '2':
    ucret=10
if ogrenci == 'e':
    ucret=ucret/2
    print("ödemeniz gereken ücret {}  ".format(ucret))"""

#21
"""for asa in range (2,a):
     if(a%asa==0):
          print("asal değil")
          break
     else: 
        print("asal")
        break"""

#22
"""sayi= input("bir sayı giriniz")
tektoplam=0
cifttoplam=0
for i in range(1,int(sayi)):
    if(i%2==0):
        cifttoplam+=i
    else:
        tektoplam+=i
        print("tek sayıların toplamı {0}".format(tektoplam))
        print("çift sayıların toplamı {0}".format(cifttoplam))"""


#23
"""yenimaas=0
maas=input("maaşı gir")
zam=input("zam oranı")
yenimaas=int(maas)+(int(maas)*int(zam)/100)
print("zamlı maaş " ,yenimaas)"""

#24
"""yukseklik=int(input("dikdörtgenin yüksekliğini giriniz "))
genislik=int(input("dikdörtgenin genişliğini giriniz"))
alan=yukseklik*genislik
print(alan)"""

#25
"""r=int(input("yarıçap giriniz"))
alan=3.14*r*r
print(alan)"""

#26
"""import random
sayi=random.randint(1,101)
tahminsayac=0
tahminlimit=3
print("1 ile 100 arasında bir sayı seçildi.")
while tahminsayac < tahminlimit:
    tahmin= int(input("tahminin nedir"))
    tahminsayac+=1
    if tahmin <sayi:
        print("daha büyük bir sayı söyleyin")
    elif tahmin > sayi:
    else:
        print("tebrikler bildiniz")
    if tahminsayac == tahminlimit:
        print("tahmin hakkınız bitti")"""

#27
"""from datetime import datetime
tarih_str = input("Tarihi gir ")
tarih = datetime.strptime(tarih_str, "%d-%m-%Y")
gun_numarasi = tarih.timetuple().tm_yday
print(f"{tarih_str} tarihi yılın {gun_numarasi}. günü.")"""

#28
"""liste=[10,44,32,78,94,66,57,42,68,92,55,90]
for i in liste:
 if(i % 5==0):
   print(i)"""

#29
"""def karakter_var_mi(metin, karakter):
    if karakter in metin:
        return True 
    else:
        return False 
metin = "Merhaba, dünya!" 
karakter = "d"  
if karakter_var_mi(metin, karakter):
    print(f"'{karakter}' karakteri metin içinde bulunmaktadır.")
else:
    print(f"'{karakter}' karakteri metin içinde bulunmamaktadır.")"""


#30
"""def cift_mi(sayi):
    return sayi % 2 == 0
sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))
toplam = 0
sayi_adedi = 0
for sayi in range(sayi1,sayi2):
    if cift_mi(sayi):
        toplam += sayi
        sayi_adedi += 1
ortalama = toplam / sayi_adedi
print(ortalama)"""

#31
"""def dikdortgen_alani(genislik, yukseklik):
    
    return genislik * yukseklik
genislik = int(input("genişliğini "))
yukseklik = int(input(" yüksekliğini "))
alan = dikdortgen_alani(genislik, yukseklik)"""

#32
"""gunler = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma"]
indeks = int(input("0-4 arası sayı gir"))
print(f"Girilen indeksteki gün: {gunler[indeks]}")"""


#33





#34
"""sayi=input("Bir sayı girin: ")
toplam=0
for rakam in sayi:
  toplam += int(rakam)
print("sayının rakamları toplamı",toplam)"""


#35
"""toplam = 0
while True:
    sayi = float(input(" sayı gir "))
    if sayi == 0:
        break  
    toplam += sayi 
print(toplam)"""
