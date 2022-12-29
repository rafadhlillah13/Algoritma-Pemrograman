## Soal
1. Ubah while-loop ini menjadi fungsi yang dapat Anda panggil, dan ganti 6 dalam pengujian (i < 6) dengan variabel. 
2. Gunakan fungsi ini untuk menulis ulang skrip untuk mencoba nomor yang berbeda. 
3. Tambahkan variabel lain ke argumen fungsi yang dapat Anda lewati yang memungkinkan Anda mengubah +1 pada baris 8 sehingga Anda dapat mengubah seberapa banyak kenaikannya. 
4. Tulis ulang skrip lagi untuk menggunakan fungsi ini untuk melihat efek apa yang terjadi.
5. Tulis untuk menggunakan for-loop dan range. Apakah Anda membutuhkan incrementor di tengah lagi? Apa yang terjadi jika Anda tidak menyingkirkannya?

## Jawaban
1. ganti 6 dalam pengujian (i < 6) dengan variabel.
```python
def loop(batas):  
   i = 0
  numbers = []

#ganti 6 dalam pengujian (i < 6) -> 10
  while i < 10:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

  return numbers
batas=int(input("masukkan batas : "))
print(f"The numbers: {loop(batas)}")

for num in numbers:
    print(num)

```
2. maaf, maksudnya nomor yang mana bang?
3. mengubah seberapa banyak kenaikannya
```python
i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i +=1 #menggunakan increment, sehingga kita dapat mengatur seberapa banyak kenaikannya
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")


print("The numbers: ", numbers)
```
4. Tulis Ulang
```python
i = 0
numbers = []

while i < 6:
  print(f"At the top i is {i}")
  numbers.append(i)

  i = i + 1
  print("Numbers now: ", numbers)
  print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
  print(num)
```
5. for loop dan range
   ```python
    def insert_to_list(n, increment=1):
      numbers = []
      i = 0
      while i < n:
        print(f"At the top i is {i}")
        numbers.append(i)
    
        i = i + increment
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    
      return numbers
    
    
    numbers = insert_to_list(10)
    for i in numbers:
      print(i)
    numbers = insert_to_list(10, 2)
    for i in numbers:
      print(i)
    
    list = insert_to_list(10, 4)
    #list akan sama dengan
    number = []
    for i in range(0, 10, 4):
      number.append(i)
    
    #jika menggunakan perulangan for kita tidak perlu mengincrement nilai i
    print(list)
    print(number)


    ```