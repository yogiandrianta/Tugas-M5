# 1. tuple jadwal_hari
jadwal_hari = ("Senin", "Selasa", "Rabu", "Kamis", "Jumat")

print(jadwal_hari)
print(type(jadwal_hari))


# 2.
koordinat = (10, 20, 30, 40, 50)

print(koordinat[2])
print(koordinat[3:5])


# 3. 
data = (10, 20, 30)


# 4. 
kumpulan_huruf = ("a", "b", "c", "a", "d", "a", "e")

print(kumpulan_huruf.index("d"))
print(kumpulan_huruf.count("a"))


# 5. Unpacking tuple
titik_lokasi = (112.79, -7.28)

longitude, latitude = titik_lokasi

print(longitude)
print(latitude)


# 6.
kendaraan = ("Motor", "Mobil", "Sepeda")

kendaraan_list = list(kendaraan)
kendaraan_list[1] = "Bus"

kendaraan = tuple(kendaraan_list)

print(kendaraan)