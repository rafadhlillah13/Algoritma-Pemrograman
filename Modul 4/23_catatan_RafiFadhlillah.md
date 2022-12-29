### Soal
1. Bagaiamana cara data di simpan di komputer?
2. Apa itu bit?
3. Apa itu byte? Apakah perbedaan dengan bit?
4. Terdapat kode di bawah ini. Apakah maksud dari setiap barisnya, dan menghasilkan output apa?
 ```python
   print(0b1011010)
   print(ord(’Z’))
   print(chr(90))
   ```
5. Setelah kita memiliki konvensi ASCII untuk menyandikan karakter menggunakan 8 bit (satu byte), kita kemudian dapat "menggabungkan" mereka untuk membuat sebuah kata, misanya "Dimas". Apakah ini bisa? Bagaimana cara kerjanya?
6. Apakah `Unicode` itu?
7. Jika memiliki byte mentah, maka harus menggunakan .decode() untuk mendapatkan string. Benar atau salah?
8. Kapan .encode() digunakan dalam python?

### Jawaban :

1. Dengan mengencode data (bahasa manusia) ke bahasa mesin (biner) 0/1 dengan satuan bit (satuan terkecil dalam komputer (0/1)), karena yang komputer tahu hanya bahasa 0/1

2. Binary digit (bit) adalah satuan terkecil dalam komputer (0/1), disebut juga bilangan biner. Biasanya dalam penyimpanan satuan ini jarang digunakan karena terlalu kecil dan menggunakan byte (8 bit), KB (Kilo byte = 1024 byte), GB (Giga byte = 1024 kb), TB (Tera byte = 1024 GB), dst..

3. Byte adalah sekumpulan bit (8 bit) maksudnya 1 byte = 8 bit, byte biasanya digunakan untuk satuan penyimpan (storage) byte dilambangkan dengan "B" (besar) sedangkan bit dilambangkan dengan "b" (kecil)

4. Terdapat kode di bawah ini. Apakah maksud dari setiap barisnya, dan menghasilkan output apa?
   ```python
   print(0b1011010)
   print(ord(’Z’))
   print(chr(90))
   ```
#### jawab:
1. Pada baris pertama `print(0b1011010)` merupakan bilangan biner yang akan di cetak/print() ke layar dalam keadaan desimal (90)
2. Pada baris kedua `print(ord('Z'))` program akan mencetak sebuah encode (integer) dari character dengan fungsi ord() encode dari 'Z' adalah 90
3. Pada baris ketiga `print(chr(90))` program akan mencetak pengembalian dari encode sebuah char (decode), dan dengan fungsi chr() akan menampilkan char dari sebuah encode (integer), decode dari 90 adalah 'Z'
4. note: ord() adalah kebalikan dari chr() dan encode di atas adalah ASCII

5. Setelah kita memiliki konvensi ASCII untuk menyandikan karakter menggunakan 8 bit (satu byte), kita kemudian dapat "menggabungkan" mereka untuk membuat sebuah kata, misalnya "Dimas". Apakah ini bisa? Bagaimana cara kerjanya?
#### Jawab: 
Bisa, coba kita implentasikan ke bahasa pemrograman python:
1. pertama kita bisa menggunakan perulangan seperti ini:
```python
d = [68, 105, 109, 97, 115]
c = ""
for i in range(len(d)):
  c = c + chr(d[i]) #menggabungkan char yang sudah di decode
print(c)
```
2. kita juga bisa menggunakan fungsi join() seperti ini:
```python
d = [68, 105, 109, 97, 115]
print(''.join(chr(d[byte]) for byte in range(len(d))))
```
  fungsi join() berfungsi untuk menggabungkan sebuah char

6. Unicode adalah suatu standar teknis yang dirancang untuk mengizinkan teks dan simbol dari semua sistem tulisan di dunia untuk ditampilkan dan dimanipulasi secara konsisten oleh komputer berdasarkan definisi tersebut dapat disimpulkan bahwa Unicode adalah pengkodean byte yang bisa diatur untuk membuat simbol atau karakter unik 

7. Benar

8. Jika ingin mengencode suatu string atau character yang terdapat karakter unik atau simbol dan menjadikan suatu bytes
