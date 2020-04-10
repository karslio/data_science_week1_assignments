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
# Deneme matrislerini de gonderebilirsiniz. Hepinize kolay gelsin


import numpy as np
import time

i = 0

start = time.time()
while True:
    a = np.random.rand(10, 10)
    b = np.random.rand(10, 10)
    c = a - b
    diagonal = np.diagonal(c)
    if np.all(diagonal > -0.1) & np.all(diagonal < 0.1):
        break
    i += 1

end = time.time()
time = end - start
with open("numpy_master.txt", "w", encoding="utf-8") as file:
    file.write("""
import numpy as np
import time

i = 0
start = time.time()
while True:
    a = np.random.rand(10, 10)
    b = np.random.rand(10, 10)
    c = a - b
    diagonal = np.diagonal(c)
    if np.all(diagonal > -0.1) & np.all(diagonal < 0.1):
        break
    i += 1

end = time.time()
time = end - start
######################################################################
""")
    file.write('subtract_matrix :' + '\n' + str(c) + '\n')
    file.write('diagonal :' + str(diagonal) + '\n')
    file.write('number_of_loops :' + str(i) + '\n')
    file.write('total_time :' + str(time / 60) + ' minutes')
