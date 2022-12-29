print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ") #meminta inputan user dan disimpan ke dalam variabel door

#percabangan 1
if door == "1": # membuat percabangan jika user menginputkan 1 maka program akan mengeksekusi code dibawah
    print("There's a giant bear here eating a cheese cake.  What do you do?") #output jika user menginputkan 1
  
    print("1. Take the cake.") 
    print("2. Scream at the bear.")
#sub percabangan 1
    bear = input("> ") #meminta inputan user kembali dan disimpan ke dalam variabel bear
    if bear == "1": #percabangan if jika user menginputkan 1 maka program akan mengeksekusi code dibawah
        print("The bear eats your face off.  Good job!") #output jika user menginputkan 1
    elif bear == "2": #percabangan elif jika user menginputkan 2 maka program akan mengeksekusi code diabawah
        print("The bear eats your legs off.  Good job!") #output jika user menginputkan 2
    else: # percabangan else jika user menginputkan nilai selain 1 dan 2 maka akan mengeksekusi code dibawah
        print(f"Well, doing {bear} is probably better.  Bear runs away.") #output jika user menginputkan nilai selain 1 dan 2

#lanjutan percabangan 1 menggunakan elif
elif door == "2": #percabngan elif jika user menginputkan nilai 2 maka akan mengeksekusi code dibawah
    print("You stare into the endless abyss at Cthulhu's retina.") #output jika user menginputkan nilai 2
  
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ") #meminta user untuk menginputkan nilai kembali dan menyimpan ke dalam variabel insanity

#sub percabangan
    if insanity == "1" or insanity == "2": #percabangan jika user menginputkan nilai 1 atau 2 maka akan mengeksekusi code dibawah
        print("Your body survives powered by a mind of jello.  Good job!")
    else:#lanjutan percabangan if jika user menginput nilai selain 1 atau 2 akan mengeksekusi code dibawah
        print("The insanity rots your eyes into a pool of muck.  Good job!") #


else:
    print("You stumble around and fall on a knife and die.  Good job!")