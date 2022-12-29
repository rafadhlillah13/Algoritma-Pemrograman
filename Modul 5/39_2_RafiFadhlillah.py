##Temukan dokumentasi Python untuk dictionary dan coba ekspor lebih banyak lagi hal-hal yang dapat anda buat.

#fungsi copy() dictionary
makanan_khas = {'jogja':'gudek', 'jakarta':'kerak telor', 'bandung':'karedok'}
#Membuat salinan dari makanan_khas
makanan_daerah = makanan_khas.copy()
print ("Makanan Khas : ",makanan_khas)
print ("Makanan Daerah : ",makanan_daerah)

#fungsi clear() dictionary
makanan_khas = {'jogja':'gudek', 'jakarta':'kerak telor', 'bandung':'karedok'}
#Mencetak semua elemen dictionary
print ("Sebelum dihapus : ",makanan_khas)
#Menghapus semua elemen dictionary
makanan_khas.clear()
print ("Setelah dihapus : ",makanan_khas)

#fungsi fromkey() dictionary
# mendefinisikan dictionary kota
kota = {'jogja', 'jakarta', 'bandung'}
# membuat dictionary ibu_kota
ibu_kota = dict.fromkeys(kota, 'Ibu Kota Provinsi')
print("Ibu Kota: ", ibu_kota)

#fungsi len() dictionary
makanan_khas = {'jogja':'gudek', 'jakarta':'kerak telor', 'bandung':'karedok'}
print ("Dictionary : ",makanan_khas)
print ("Jumlah Elemen : ",len(makanan_khas))

#fungsi get() dictionary
# mendefinisikan dictionary
makanan_khas = {'jogja':'gudek', 'jakarta':'kerak telor', 'bandung':'karedok'}

# mencari elemen
a = makanan_khas.get('jogja')
b = makanan_khas.get('jakarta')
c = makanan_khas.get('bandung')

#mencetak hasil
print("a: ", a)
print("b: ", b)
print("c: ", c)

#fungsi items() dictionary
makanan_khas = {'jogja':'gudek', 'jakarta':'kerak telor', 'bandung':'karedok'}
a = makanan_khas.items()
print(a)

#fungsi keys() dictionary
makanan_khas = {'jogja':'gudek', 'jakarta':'kerak telor', 'bandung':'karedok'}
a = makanan_khas.keys()
print(a)

#fungsi values() dictionary
makanan_khas = {'jogja':'gudek', 'jakarta':'kerak telor', 'bandung':'karedok'}
a = makanan_khas.values()
print(a)