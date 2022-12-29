## Soal
1. Carilah contoh best practice dalam hal if-statements dan loops!
2. Pasti teman-teman sudah mengetahui tentang debugging. Apakah debugging itu? Apakah ada tips dalam melakukan debugging?

## Jawaban
1. Berikut adalah contoh dari if-statements within for loops
```python
for i in range(100):
    if i % 3 == 0 and i % 5 == 0:
        print('Rafi')
    elif i % 3 == 0:
        print('Fadhlillah')
    elif i % 5 == 0:
        print('Rafi_Fadhlillah')
    else:
        print('-')
```
2. Debugging adalah proses mengidentifikasi dan menghapus bug atau error di dalam kode.Bug inilah menyebabkan sebuah aplikasi atau software tidak berjalan dengan semestinya. Misalnya, gagal login, error saat input data, disfungsi fitur, blue screen, dll.Karena sistem pengkodean suatu program biasanya rumit dan kompleks, maka satu saja kesalahan kode dapat berpengaruh pada keseluruhan program. Tidak heran juga kalau debugging bisa memakan waktu lebih lama dibandingkan saat menulis program itu sendiri. Itu kenapa proses debug sangat penting dilakukan. Baik sebelum perilisan aplikasi maupun sesudahnya.<br>

## Tips Melakukan debugging 
  1. Melakukan Exception Handling 
  2. Print/Check semua code
  3. Use of Logging Module
  4. Menggunakan pdb, pdb adalah alat debugging bawaan Python. Ini dapat digunakan dari command line, di dalam interpreter, atau di dalam program untuk membantu developer menjalankan program dalam single step mode. Developer dapat menggunakan pdb debugger untuk menyetel breakpoint dan memeriksa source code.