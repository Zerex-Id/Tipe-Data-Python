daftar_buku = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
print('\nTampilkan variable daftar_buku')
print(daftar_buku)

print('\nProses semua dengan for in')
for buku in daftar_buku:
    print(buku)

print('\nTampilkan isi daftar_buku pada indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[2])

print('\nTampilkan dengan for in range')
for buku in range(0, len(daftar_buku)):
    print(daftar_buku[buku])

print('\nTampilkan dengan for in range, dimana tipe data tiap elemen berbeda2')
daftar_buku = [2, 'Kenji Volume 2', -314, 3.14]
for buku in range(0, len(daftar_buku)):
    print(daftar_buku[buku])

print('\nKembalikan nilai awal daftar_buku')
daftar_buku = ['1. Seven Habits', '2. How to Influence People', '3. First Things First', '4. 4DX']
print('\nTambahkan 1 buku baru')
daftar_buku.append('Dunia Matematika kelas 5')
for buku in range(0, len(daftar_buku)):
    print(daftar_buku[buku])

print('\nClear list')
daftar_buku.clear()
for buku in range(0, len(daftar_buku)):
    print(daftar_buku[buku])

print('\nGanti elemen pertama')
daftar_buku = ['1. Seven Habits', '2. How to Influence People', '3. First Things First', '4. 4DX']
daftar_buku[0] = '1. Eight Habits'
for buku in range(0, len(daftar_buku)):
    print(daftar_buku[buku])

print('\nAmbil elemen ke-2')
ambil = daftar_buku.pop(1)
for buku in range(0, len(daftar_buku)):
    print(daftar_buku[buku])

print('\nTampilkan buku yang diambil')
print(ambil)

print('\nPop')
daftar_buku.pop()
for buku in range(0, len(daftar_buku)):
    print(daftar_buku[buku])

print('\nPop -1')
daftar_buku = ['1. Seven Habits', '2. How to Influence People', '3. First Things First', '4. 4DX']
daftar_buku.pop(-4)
for buku in range(0, len(daftar_buku)):
    print(daftar_buku[buku])
