i = 0 #mendeklarasi variabel i = 0
numbers = [] #membuat list kosong dan disimpan ke variabel numbers

while i < 6: #perulangan while ketika nilai i < 6 maka akan mengeksekusi code dibawah
    print(f"At the top i is {i}") #menggunakan f string 
    numbers.append(i) #menambahkan nilai ke list i

    i = i + 1 #nilai i akan selalu bertambah 1 jika perulangan terjadi
    print("Numbers now: ", numbers) #mencetak variabel numbers
    print(f"At the bottom i is {i}") #mencetak list paling dasar/bawah


print("The numbers: ")

for num in numbers: #menyingkat variabel numbers => num
    print(num) #mencetak num