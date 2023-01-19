"""
kendisine gönderilen sayılardan sadece palindrom
olanları toplayan
diğerlerini de bu toplamdan çıkaran ve geri
döndüren python fonksiyonunu yazınız.
"""

def polinDRAM(*dram):
     toplam=0
     for sayi in dram:
         if str(sayi)==str(sayi)[::-1]:
             toplam += sayi
         else:
             toplam -= sayi
     return toplam

print(polinDRAM(11,55,101,20,44,10,40,50))