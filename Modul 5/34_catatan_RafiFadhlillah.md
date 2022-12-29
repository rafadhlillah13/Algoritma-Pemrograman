## Soal

1. Tipe data apa saja yang bisa dimasukkan ke dalam list?
2. list_buah[0:-1], apakah maksud potongan kode di samping?
3. Indeks negatif dalam list apakah dimulai dari -1 atau 0?
4. Apakah fungsi list kosong?
5. Tuliskan dan terapkan fungsi-fungsi bawaan dari list!
6. Buatlah contoh list multi dimensi, contohnya: [['Dimas', 'Wahyu', 'Dhoni'], ['Lanang', ' Gokil'], 'Dimas' ]
7. Jelaskan Baris Perbaris Pada kode Diatas, menggunakan feature comment # disetiap barisnya!

## Jawaban
1. List dapat diisi dengan tipe data apa saja seperti string, integer, float, double, boolean, object, dll. Kita juga bisa mencampur isinya.
2. Akan mengoutputkan data list dengan indeks 0 sampai indeks sebelum -1
3. Indeks negatif dimulai dari tergantung banyaknya data dan diakhiri dengan indeks -1. contoh kita punya list[a,b,c,d,e,f,g,h] -> data disamping jika menggunakan format indeks negatif karena data dalam list ada 8 elemen maka indeks akan dimulai dari -8(a) dan diakhiri dengan indeks -1(h)
4. list_buah = ['Pisang', 'Nanas', 'Melon', 'Durian']
   pada list_buah[0:-1] tidak kosong tetapi akan mengoutputkan pisang,nanas,melon karena dibatasi indeks -1 maka durian tidak dioutoputkan
5. Python memiliki beberapa fungsi bawaan yang langsung dapat kita gunakan. Secara umum, berikut ini adalah beberapa fungsi-fungsi dari tipe data list yang bisa kita manfaatkan untuk menyelesaikan berbagai macam permasalahan:

- append()	Menambahkan elemen baru pada akhir data list
- clean()	Menghapus semua elemen pada data list
- copy()	Mengembalikan hasil duplikasi dari data list
- count()	Mengembalikan jumlah elemen yang ditentukan pada data list
- extend()	Menambahkan elemen dari tipe data list (atau tipe data lain) ke posisi akhir dari data list tertentu
- index()	Mengembalikan indeks pertama dari elemen yang ditentukan
- insert()	Menambahkan elemen baru ke dalam data list pada posisi tertentu
- pop()	Menghapus elemen pada akhir data list atau pada elemen yang ditentukan
- remove()	Menghapus elemen pada nilai yang ditentukan
- reverse()	Membalik posisi pada tiap-tiap elemen data list
- sort()	Mengurutkan data list
6. bahasa = [["java","python","c"],["ruby","javascript","php"],["dart","c++","pascal"]]
7. 