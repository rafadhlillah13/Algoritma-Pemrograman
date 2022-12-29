# Tulis fungsi yang menghitung volume bola jika diketahui jari-jarinya!
# rumus volume bola = 4⁄3 πr³

def volume_bola(pi,r):
  v = (4/3)*pi*(r**3)
  return v
  
#diketahui r = 7
hasil = volume_bola(3.14, 7)
print("Volume bola -> r=7 = ", hasil)