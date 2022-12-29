# Tulis fungsi yang memeriksa apakah suatu angka berada dalam rentang tertentu (termasuk tinggi dan rendah)

def rentang (range):
  nilai = range(a, b)
  return nilai

print ('Masukkan rentang angka minimum = ')
a = int(input())
print ('Masukkan rentang angka maksimum = ')
b = int(input())
print ('Masukkan angka yang akan di cek ')
c = int(input())

if c in  range(a,b) and(c is max(range(a,b))):
  print('Angka yang anda masukkan termasuk yang tertinggi')

elif c in  range(a,b) and(c is min(range(a,b))):
  print('Angka yang anda masukkan termasuk yang terendah')
elif c in range (a,b) and(c is not max(range(a,b))) and(c is not max(range(a,b))):
  print('Angka termasuk kedalam range namun tidak termasuk yang tertinggi atau terendah')
elif c is not range (a,b) and(c is not max(range(a,b))) and(c is not max(range(a,b))):
  print('Angka yang anda masukkan tidak termasuk kedalam range')