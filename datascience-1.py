# Numpy ile ilgili 44 soruluk Odev
# 1.	Numpy’da Vektor ve Matrisin farkini tek cumle ile ifade ediniz.
#       vektor tek boyutlu MAtris cok boyutludur.
# 2.	10 elemanli bir listeden NumPy Array’i olusturunuz.

import numpy as np

a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(type(a), a, sep="\n")

# <class 'numpy.ndarray'>
# [0 1 2 3 4 5 6 7 8 9]

# 3.	Icerisinde ‘0’ lar olan, ve veri tipi integer olan 10X10’luk bir matris olusturunuz.

np_zeros = np.zeros((10, 10), dtype='int32')
print(np_zeros)

# [[0 0 0 0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0 0 0 0]
#  [0 0 0 0 0 0 0 0 0 0]]

# 4.	Icerisinde ‘1’ ler olan, veri tipi float olan 10X10’luk bir matris olusturunuz.
np_one_float = np.ones((10, 10), dtype='float32')
print(np_one_float)

# [[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]]

# 5.	Icerisinde ‘9’ lar olan, veri tipi integer olan 10X10’luk bir matris olusturunuz.
np_9 = np.full((10, 10), 9, dtype='float32')
print(np_9)
# [[9. 9. 9. 9. 9. 9. 9. 9. 9. 9.]
#  [9. 9. 9. 9. 9. 9. 9. 9. 9. 9.]
#  [9. 9. 9. 9. 9. 9. 9. 9. 9. 9.]
#  [9. 9. 9. 9. 9. 9. 9. 9. 9. 9.]
#  [9. 9. 9. 9. 9. 9. 9. 9. 9. 9.]
#  [9. 9. 9. 9. 9. 9. 9. 9. 9. 9.]
#  [9. 9. 9. 9. 9. 9. 9. 9. 9. 9.]
#  [9. 9. 9. 9. 9. 9. 9. 9. 9. 9.]
#  [9. 9. 9. 9. 9. 9. 9. 9. 9. 9.]
#  [9. 9. 9. 9. 9. 9. 9. 9. 9. 9.]]

# 6.	5 ile 25 arasinda, 3’er 3’er atlayan tek boyutlu bir Array olusturunuz.

print(np.arange(5, 25, 3))  # [ 5  8 11 14 17 20 23]

# 7.	-1 ile 1 arasinda 30 adet Array olusturunuz.
print(np.linspace(-1, 1, 30))
# [-1.         -0.93103448 -0.86206897 -0.79310345 -0.72413793 -0.65517241
#  -0.5862069  -0.51724138 -0.44827586 -0.37931034 -0.31034483 -0.24137931
#  -0.17241379 -0.10344828 -0.03448276  0.03448276  0.10344828  0.17241379
#   0.24137931  0.31034483  0.37931034  0.44827586  0.51724138  0.5862069
#   0.65517241  0.72413793  0.79310345  0.86206897  0.93103448  1.        ]

# 8.	0 ile 30 arasinda 5x6’lik bir matris olusturun.
print(np.random.randint(0, 30, (5, 6)))
# [[17 27 16 14 22  0]
#  [ 9  3 29 20 13 28]
#  [25  3 19 19 29 23]
#  [12  1 23  6 14 21]
#  [27  6  8 12  5 29]]

# 9.	Kosegenleri 1 olan 10x10’luk bir matris olusturunuz.
print(np.eye(10))
# [[1. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 1. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 1. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 1. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 1. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 1. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 1. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 1.]]

# 10.	0 ile 10 arasinda 5x10’lik bir matris olusturun. (integer) ve bu matrisin;
np_info = np.random.randint(0, 10, (5, 10))
print(np_info)
# a.	eleman sayisini
print("Toplam eleman sayisi =  ", np_info.size)
# b.	boyut bilgisini/sayisini
print("satir, sutun bilgisi =  ", np_info.shape)
# c.	satir X sutun bilgisini
print("Boyut sayisi =  ", np_info.ndim)
# d.	veri tipini numpy metodlariyla yazdiriniz.
print("Veri tipi =  ", np_info.dtype)

# 11.	0 ile 10 arasindaki degerlerden olusan 3 adet 4x7’lik bir matris olusturunuz. (3 boyutlu bir matris olusturulacak)
np_3boyut = np.random.randint(10, size=(3, 4, 7))
print(np_3boyut)
# [[[7 9 4 0 2 6 2]
#   [1 2 0 6 3 7 6]
#   [5 3 7 9 5 6 1]
#   [8 3 6 3 1 4 0]]

#  [[7 4 2 8 4 8 5]
#   [7 0 6 8 4 9 2]
#   [0 2 1 7 6 3 7]
#   [5 6 6 2 3 3 4]]
#
#  [[4 8 2 5 6 0 5]
#   [8 8 9 3 2 3 6]
#   [3 8 7 6 5 3 7]
#   [1 4 4 8 4 9 0]]]

# 12.	Bir vektor olusturunuz ve daha sonrasinda ayni vektoru bir matrise ceviriniz. (boyut sayisini degistirin.)
np.arange(1, 10)
print(np.arange(1, 10).reshape(3, 3))

# 13.	4 tane ayri tek boyutlu array’i birlestirerek bir array olusturunuz.
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
z = np.array([7, 8, 9])
t = np.array([4, 5, 6])
print(np.concatenate([x, y, z, t]))  # [1 2 3 4 5 6 7 8 9 4 5 6]

# 14.	2 boyutlu bir vektor ve bir matris olusturun(ayri ayri), bu iki arrayi numpy metodlarini kullanarak sutun bazli birlestiriniz,
a = ([[1, 2, 3],
      [4, 5, 6]])

b = np.array([[9, 8, 7],
              [6, 5, 4]])

a_b = np.hstack([a, b])
print(a_b)
# [[1 2 3 9 8 7]
#  [4 5 6 6 5 4]]

# 15.	Numpy’da “axis=1” ve “axis=0”  arasinda ne fark vardir. Teorik olarak yaziniz?

# 16.	Farkli boyutlardaki arraylari satin ve sutun bazli ayri ayri birlestiriniz.
a = np.array([[1],
              [4]])

b = np.array([[9, 8, 7],
              [6, 5, 4],
              [9, 5, 4]])
# print(np.vstack([a, b]))
# ValueError: all the input array dimensions for the concatenation axis must match exactly,
# but along dimension 1, the array at index 0 has size 1 and the array at index 1 has size 3
# print(np.hstack([a, b]))
# ValueError: all the input array dimensions for the concatenation axis must match exactly,
# but along dimension 0, the array at index 0 has size 2 and the array at index 1 has size 3

# 17.	10 elemanli bi liste olusturunuz ve bu listeyi Numpy metodlariyla bolerek(split) 4 ayri array olusturunuz.

liste = np.random.randint(6, size=10)
k, l, c, d = np.split(liste, [2, 5, 7])
print(liste)
print(k, l, c, d)

# 18.	Random bir array olusturunuz ve bu arrayi buyukten kucuge dogru siralayiniz.
#       Ve bu siralamadan sonra hangi elemanin hangi indexte oldugunu gosteren bir metod uygulayiniz.
a = np.random.randint(10, size=(3, 5))  # 3x5 iki boyutlu matris
a.sort()
print(a)
print(a[0, 1])
print(np.where(a[0, 1]))

# 19.	20 elemanli random bir vektor olusturunuz. Bu vektorun 3. 5. ve 7. elemanlarina ulasin.
vektor = np.random.random(20)
print(vektor, vektor[3], vektor[5], vektor[7], sep='\n')
# 20.	10 elemanli random bir vektor olusturunuz ve bu arrayin  4. elemanini farkli bir sayiyla degistiriniz.
vektor = np.random.random(10)
vektor[4] = 999
print(vektor)

# 21.	“Diagonal Matrix” ve “Trace Matrix”  kavramlari hakkinda kucuk bir arastirma yapip bunlarin ne oldugunu belirten kucuk bir aciklama yaziniz.
# DIAGONAL MATRIS SOL UST KOSEDEN SAG ALT KOSEYE KADAR OLAN KOSEGENLERIN SIFIRDAN FARKLI OLDUGU VE DIGER TUM ELEMANLARININ SIFIR OLDUGU MATRISTIR.
# Trace Matrix de bu elemanlarin toplamidir.


# 22.	5x5’lik Diagonal bir matris olusturunuz ve Diagonaline denk gelen indexlere ulasiniz.(ayri ayri)

matrix = np.random.rand(5, 5)
print(matrix)
for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        if x == y:
            print(matrix[x][y], [x, y])
            break

# [[0.83012078 0.42648365 0.36046359 0.62257443 0.17808507]
#  [0.46285012 0.72130592 0.53608289 0.66651713 0.49710748]
#  [0.56196162 0.53176396 0.33133055 0.58240732 0.34668266]
#  [0.75814803 0.01172247 0.08679601 0.19559848 0.03464192]
#  [0.86317345 0.79789596 0.40572314 0.09815231 0.95961094]]
# 0.8301207847020672 [0, 0]
# 0.7213059156987719 [1, 1]
# 0.33133055116911103 [2, 2]
# 0.1955984802355546 [3, 3]
# 0.959610940069607 [4, 4]


# 23.	10 ile 20 arasinda bir vektor olusturunuz. Ve 3. indexten son indexe kadar olan degerleri yazdiriniz.
a = np.arange(10, 20)
print(a[3:])

# 24.	10X10 luk bir matris olusturunuz ve ;
a = [[2, 1, 9, 1, 1, 6, 5, 7, 9, 4],
     [2, 8, 8, 6, 6, 7, 8, 2, 4, 7],
     [3, 0, 5, 7, 3, 3, 0, 2, 3, 0],
     [4, 6, 5, 9, 0, 9, 7, 6, 1, 7],
     [5, 2, 0, 0, 9, 4, 5, 9, 4, 8],
     [4, 4, 7, 6, 3, 8, 5, 5, 8, 0],
     [7, 6, 4, 3, 0, 3, 3, 4, 4, 5],
     [5, 1, 3, 4, 7, 9, 2, 9, 5, 3],
     [7, 5, 4, 7, 3, 1, 7, 8, 8, 3],
     [9, 7, 1, 7, 3, 0, 7, 5, 7, 9]]
a = np.array(a)
#  3.satir ve 5.sutuna ulasiniz.
print(a[3, 5])
# a.	5.sutunun tum satirlarina ulasiniz.
print(a[:, 5])  # [6 7 3 9 4 8 3 9 1 0]
# b.	Tum sutunlarin 2.satirlarina ulasiniz.
print(a[2, :])  # [3 0 5 7 3 3 0 2 3 0]
# c.	tum sutunlarin 2 ile 7 arasindaki satirlarina ulasiniz.
print(a[2:7, :])
# [[3 0 5 7 3 3 0 2 3 0]
#  [4 6 5 9 0 9 7 6 1 7]
#  [5 2 0 0 9 4 5 9 4 8]
#  [4 4 7 6 3 8 5 5 8 0]
#  [7 6 4 3 0 3 3 4 4 5]]

# d.	satir indexi 2’den 5’e ve sutun indexi 3 den 7’ye kadar olan degerlere ulasiniz.
print(a[2:5, 3:7])
# [[7 3 3 0]
#  [9 0 9 7]
#  [0 9 4 5]]
# e.	satir indexi 5’den en sona ve sutun indexi en bastan 4’e kadar olan degerlere ulasiniz.
print(a[5:, :4])
# f.	sutun indexi sadece 3, 6,9 olan kolonlarin(sutunlarin), tum satirlarina ulasiniz.
print(a[(3, 6, 9), :])

# g.	5. indexli satir ve 5.indexli sutuna denk gelen degeri, dogum yilinizla degistiriniz.
a[5][5] = 1998
print(a)
# 25.	0’dan 50’ye kadar 5’er 5’er atlayarak giden bir array olusturunuz(tek boyutlu) ve numpy metodlariyla asagidaki islemleri uygulayin;

a = np.arange(0, 50, 5)
print(a)
# [ 0  5 10 15 20 25 30 35 40 45]
#  .	20 den buyuk olan kac deger var.
print(sum(a > 20))  # 5
# a.	30’dan kucuk kac deger var
print(sum(a < 30))  # 6
# b.	icerisinde 33 gecen kac deger var
print(sum(a == 33))
# c.	olusturulan arrayin tum elemanlarini 5 ile carpin.
print(a * 5)
# d.	olusturulan arrayin tum elemanlarinin 2 ile bolumunden kalanlari yazdiriniz.
print(a % 2)
# 26.	0 ile 1 arasinda 50 elamanli bir array olusturunuz ve;
a = np.linspace(0, 1, 50)
print(a)

#   	orlamasini aliniz.
print(np.mean(a))
# a.	standart sapmasini aliniz.
print(np.std(a))
# b.	varyansini aliniz.
print(np.var(a))
# c.	median’ini aliniz.
print(np.median(a))
# d.	en kucuk degeri bulunuz.
print(np.min(a))
# e.	en buyuk degeri bulunuz.
print(np.max(a))

# Master odev ;
# Bir dongu icerisinde random olacak sekilde iki tane 20x20’luk matris uretin ve bu matrislerin farklarini alin.
# Ve fark matrisinin diagonali,  -0.1 ile 0.1  arasinda olana kadar bu islemi tekrarlayin.
# Istenilen matris bulundugunda program dursun ve  toplam kac dongunun kuruldugunu,
# ne kadar sure icinde buldugunu ve  istenilen  matrisi  print ile birlikte ekrana yazdiriniz...
# Tavsiye: 20 x 20 luk matrisin bulunmasi saatler surebilir. Bu yuzden algoritmanizin dogrulugunu test etmek icin
# once 4x4, 5x5 gibi kucuk matrislerde deneyebilirsiniz. Ve matris sayisisini arttirarak en son 20x20 u deneyebilirsiniz.
# Matris uretme islemini np.random.random((axb)) fonksiyonu ile yapabilirsiniz.(size kalmis) 1:30
# Cuma aksamina kadar odevlerin hepsini gondermenizi rica ediyorum.
# Ayrica, matris odevinin ekran goruntusunu yada ekran videosunu gruba atmanizi istiyorum.
# Deneme matrislerini de gonderebilirsiniz. Hepinize kolay gelsin.
#
# Toplam 45 Soru
#
