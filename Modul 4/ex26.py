# Soal
#1. Perbaiki kode di atas, program apakah di atas? Jelaskan secara singkat!

# Jawaban

from sys import argv #import argv dari sys

print("How old are you?", end=' ') 
age = input() #input nilai variable
print("How tall are you?", end=' ')
height = input() #input nilai variable
print("How much do you weigh?", end=' ')
weight = input() #input nilai variable

#menampilkan nilai variable dengan f string
print(f"So, you're {age} old, {height} tall and {weight} heavy.") 

script, filename = argv #deklarasi filename sebagai argv (sebuah file)

txt = open(filename) #membuka file 

print(f"Here's your file {filename}:") #menampilkan nama file
print(txt.read()) #menampilkan isi file

print("Type the filename again:")
file_again = input("> ") #input file kembali 

txt_again = open(file_again) #membuka file

print(txt_again.read()) #menampilkan isi file

print("Let's practice everything.")
#contoh penggunaan escape character
print('You\'d need to know \'bout escapes \n with \\ that do \n newlines and \t tabs.') 

#string lebih dari 1 baris
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")
print(poem)
print("--------------")


five = 10 - 2 + 3 - 6 # -6 agar 5
print(f"This should be five: {five}")

#fungsi secret_formula()
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates #return fungsi sebanyak 3 nilai


start_point = 10000
#assigment beans, jars, crates sebagai nilai dari return fungsi secara urut
beans, jars, crates = secret_formula(start_point) 

# remember that this is another way to format a string
#menampilkan nilai variable dengan .format()
print("With a starting point of: {}".format(start_point)) 
# it's just like with an f"" string
#menampilkan beans, jars, dan crates
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10 #assigment nilai start_point sebelumnya dibagi 10

#menampilkan return nilai fungsi tanpa assigment variable beans, jars, dan crates
print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))



people = 20
cates = 30
dogs = 15


if people < cates:
    print ("Too many cats! The world is doomed!") #jika people lebih kecil(sedikit) dari cates

if people > cates:
    print("Not many cats! The world is saved!") #jika people lebih besar(banyak) dari cates

if people < dogs:
    print("The world is drooled on!") #jika people lebih kecil(sedikit) dari dogs

if people > dogs:
    print("The world is dry!") #jika people lebih besar(banyak) dari dogs


dogs += 5 #nilai dogs ditambah 5

if people >= dogs:
    #jika people lebih besar(banyak) atau sama dengan(sama banyaknya) dogs
    print("People are greater than or equal to dogs.") 

if people <= dogs:
    #jika people lebih kecil(sedikit) atau sama dengan(sama banyaknya) dogs
    print("People are less than or equal to dogs.")


if people == dogs:
  #jika people sama dengan(sama banyaknya) dogs
    print("People are dogs.") #maka people adalah dogs

""" program di atas adalah program di mana awal meminta input nilai age, height, weight lalu menampilkannya kemudiaan program akan membaca isi file yang di input pada argv(argumen variable) ketika menjalankan file lalu program meminta input file kembali untuk dibaca isinya, kemudian program melakukan operasi aritmatika yang hasilnya 5 dan ditampilkan, kemudian program mempunyai fungsi secret_formula yang memiliki 1 argumen (start_point) fungsi tersebut mereturn sebanyak 3 nilai sekaligus, lalu kita ditunjukan cara menampilkan 3 nilai tersebut secara urut dengan mengassigment kedalam variable dan tidak perlu mengassigment, kemudian terakhir program menampilkan sebuah string teks dengan logika if (jika terpenuhi maka akan ditampilkan)"""