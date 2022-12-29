## Soal
1. Mengapa kode di bawahnya harus diindentasi empat spasi?
2. Apa yang terjadi jika kode yang dibuat tidak menjorok?
3. Apa yang terjadi jika kita mengubah nilai awal untuk orang, kucing, dan anjing?
4. Apakah maksud +=?


## Jawab
1. Menurut panduan PEP 8, penulisan kode python lebih disukai menggunakan spasi. Dan selalu gunakan 4 spasi untuk indentasi. akan tetapi sebenarnya ketika kita menuliskan fungsi percabangan dan kita tekan enter maka otomatis akan identasi namun kurang dari 4 spasi lebih tepatnya 2 tab tetapi program akan tetap berjalan.
2. Akan terjadi error (IdentationError : expected an indented block)
3. Jika kita mengubahnya maka hasilnya juga akan berubah sesuai dengan nilai awalnya contohnya jika kita mengganti dogs = 15 -> dogs = 50 maka hasilnya yang tadinya "The world is dry!" -> "The world is drooled on!" karena pada saat dogs = 15 nilainya lebih kecil dari people yang nilainya 20 sedangkan ketika diganti dogs = 50 maka nilai dogs akan lebih besar dari people sehingga akan menghasilkan output yang berbeda.
4. '+=' sebenarnya sama seperti penjumlahan pada umumnya hanya saja kita dapat menyingkatnya atau menulis dalam bentuk lain menjadi seperti operator diatas contoh :
   ```
   a = 1
   a += 10
   print(a)
    
  ```
   program diatas akan mengoutputkan 11 karena program akan menjumlahkan 1 + 10 = 11