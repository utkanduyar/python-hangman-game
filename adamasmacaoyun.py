import random
harfekle=list()
def randomkelime():
    kelimeler=["araba","ucak","bardak"]
    kelime_ipucu=["karada giden bir alet","havada giden bir alet","su içmemize yarayan bir obje"]
    kelime=random.choice(kelimeler)
    if kelimeler[0]==kelime:
       ipucu=kelime_ipucu[0]
       print(ipucu)
       kelimesayısı=len(kelime)
       bölünmus=[]
       while kelimesayısı!=0:
         bölünmus.append("___")
         kelimesayısı-=1
       print(bölünmus)
       for i in bölünmus:
          harfekle.append(i)
       verialmaeklemevekontrol(kelime)  
    elif kelimeler[1]==kelime:
        ipucu=kelime_ipucu[1]
        print(ipucu)
        bölünmus=[]
        kelimesayısı=len(kelime)
        while kelimesayısı!=0:
          bölünmus.append("___")
          kelimesayısı-=1
        print(bölünmus)
        for i in bölünmus:
          harfekle.append(i)
        verialmaeklemevekontrol(kelime)
    elif kelimeler[2]==kelime:
        ipucu=kelime_ipucu[2]
        print(ipucu)
        bölünmus=[]
        kelimesayısı=len(kelime)
        while kelimesayısı!=0:
         bölünmus.append("___")
         kelimesayısı-=1
        print(bölünmus)
        for i in bölünmus:
          harfekle.append(i)
        verialmaeklemevekontrol(kelime)
def verialmaeklemevekontrol(sözcük):
  harfgirsin=str(input("lütfen bir harf giriniz :"))
  sıragirsin=int(input("hangi sıraya ekleyceğinizi seçin en düşük 0. sıra vardır! :"))
  harfekle.insert(sıragirsin,harfgirsin)
  harfekle.remove("___")
  print(harfekle)
  dosya1=open("sss.txt","w")
  dosya1.write(str(sözcük))
  dosya1.close()
print("adam asmaca oyununa hoş geldiniz :) kelime ipucu ağaşıda verildi")            
randomkelime()   