def tek_cift_bulma(sayi):
    if sayi % 2 == 0:
        print(f"{sayi} bir çift sayıdır.")
    else:
        print(f"{sayi} bir tek sayıdır.")

def sayilari_siralama(sayi1, sayi2, sayi3):
    sayilar = [sayi1, sayi2, sayi3]
    sayilar.sort(reverse=True)
    print("Büyükten küçüğe sıralanmış sayılar: ", sayilar)

def asal_sayi_bulma(sayi):
    if sayi < 2:
        print(f"{sayi} bir asal sayı değildir.")
        return
    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            print(f"{sayi} bir asal sayı değildir.")
            return
    print(f"{sayi} bir asal sayıdır.")

while True:
    print("\n(1) Girilen sayının Tek Yada Çift Olduğunu Bulma")
    print("(2) Girilen 3 sayıyı büyükten küçüğe sıralama")
    print("(3) Girilen Sayının Asal sayı olup olmadığını bulma")
    print("Çıkmak için -1'e basınız.")

    secim = int(input("Seçiminizi Giriniz (1/2/3): "))

    if secim == -1:
        print("Çıkılıyor...")
        break

    elif secim == 1:
        sayi = int(input("Bir sayı giriniz: "))
        tek_cift_bulma(sayi)

    elif secim == 2:
        sayi1 = int(input("1. sayıyı giriniz: "))
        sayi2 = int(input("2. sayıyı giriniz: "))
        sayi3 = int(input("3. sayıyı giriniz: "))
        sayilari_siralama(sayi1, sayi2, sayi3)

    elif secim == 3:
        sayi = int(input("Bir sayı giriniz: "))
        asal_sayi_bulma(sayi)

    else:
        print("Yanlış değer girdiniz, lütfen tekrar deneyiniz.")
