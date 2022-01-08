number=input("Kullanicidan bir sayi giriniz:")
lenght=len(number)
toplam=0
for i in number:
      toplam+=int(i)**lenght
if str(toplam)==number:
      print('bu sayi armstrong sayisidir')
else:
     print('bu sayi bir armstrong sayisi degildir')   