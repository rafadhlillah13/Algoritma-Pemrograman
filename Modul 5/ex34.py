# Membuat List kosong
warna = []

# Membuat list dengan isi 1 item
hobi = ["membaca"]

# List lebih dari satu
buah = ["jeruk", "apel", "mangga", "duren"]

# Mencampur isinya
laci = ["buku", 21, True, 34.12]

# Mengambil nilai dari list
# Kita punya list nama-nama buah
buah = ["apel", "anggur", "mangga", "jeruk"]

# Misanya kita ingin mengambil mangga
# Maka indeknya adalah 2
print (buah[2])

# Menampilkan list
# list kosong
list_kosong = [] 

# list yang berisi kumpulan string
list_buah = ['Pisang', 'Nanas', 'Melon', 'Durian']

# list yang berisi kumpulan integer
list_nilai = [80, 70, 90, 60]

# list campuran berbagai tipe data
list_jawaban = [150, 33.33, 'Presiden Sukarno', False]

print('list_kosong:', list_kosong) #mengoutputkan list kosong
print('list_buah:', list_buah) #mengoutputkan elemen list_buah
print('list_nilai:', list_nilai) #mengoutputkan elemen list_nilai
print('list_jawaban:', list_jawaban) #mengoutputkan elemen list_jawaban

print(list_buah[0]) #mengoutputkan elemen list_buah indeks ke 0 -> Pisang
print(list_buah[2]) #mengoutputkan elemen list_buah indeks ke 2 -> Melon
print(list_buah[1]) #mengoutputkan elemen list_buah indeks ke 1 -> Nanas
print(list_buah[3]) #mengoutputkan elemen list_buah indeks ke 3 -> Durian

# Indeks negatif
print(list_buah[-1]) #mengoutputkan elemen list_buah indeks negatif -1 -> Durian
print(list_buah[-2]) #mengoutputkan elemen list_buah indeks negatif -2 -> Melon
print(list_buah[-3]) #mengoutputkan elemen list_buah indeks negatif -3 -> Nanas
print(list_buah[-4]) #mengoutputkan elemen list_buah indeks negatif -4 -> Pisang

#Slicing list
list_buah = ['Pisang', 'Nanas', 'Melon', 'Durian']

print(list_buah[0:1]) #mengoutputkan elemen list mulai dari indeks 0 sampai sebelum 1 -> Pisang
print(list_buah[0:2]) #mengoutputkan elemen list mulai dari indeks 0 sampai sebelum 2 -> Pisang, Nanas
print(list_buah[1:3]) #mengoutputkan elemen list mulai dari indeks 1 sampai sebelum 3 -> Nanas, Melon
print(list_buah[0:-1]) #mengoutputkan elemen list mulai dari indeks 0 sampai sebelum -1 -> Pisang, Nanas, Melon
print(list_buah[-1:-3]) #mengoutputkan elemen list mulai dari indeks -1 sampai sebelum -3 -> [] list kosong
print(list_buah[-1:3]) #mengoutputkan elemen list mulai dari indeks -1 sampai sebelum 3 -> [] list kosong
print(list_buah[-3:-1]) #mengoutputkan elemen list mulai dari indeks -3 sampai sebelum -1 -> Nanas, Melon