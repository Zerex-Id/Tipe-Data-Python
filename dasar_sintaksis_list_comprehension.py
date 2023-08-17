print('\nPerintah del')
daftar_buku = ['1. Seven Habits', '2. How to Influence People', '3. First Things First', '4. 4DX']
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension')
daftar_buku = ['1. Seven Habits', '2. How to Influence People', '3. First Things First', '4. 4DX']
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension start')
daftar_buku = ['1. Seven Habits', '2. How to Influence People', '3. First Things First', '4. 4DX']
del daftar_buku[0:-2] #START:END
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension start:end:step')
daftar_buku = ['1. Seven Habits', '2. How to Influence People', '3. First Things First', '4. 4DX']
del daftar_buku[0::2] #START:END:STEP
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat List Baru')
daftar_buku = ['1. Seven Habits', '2. How to Influence People', '3. First Things First', '4. 4DX']
daftar_buku_baru = daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
print('\nMembuat List Baru')
del daftar_buku[:]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat List Baru dengan comprehension: ganjil')
daftar_buku = ['1. Seven Habits', '2. How to Influence People', '3. First Things First', '4. 4DX']
daftar_buku_baru = daftar_buku[0::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat List Baru dengan comprehension: genap')
daftar_buku = ['1. Seven Habits', '2. How to Influence People', '3. First Things First', '4. 4DX']
daftar_buku_baru = daftar_buku[1::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat List Baru dengan comprehension: buang diujung')
daftar_buku = ['1. Seven Habits', '2. How to Influence People', '3. First Things First', '4. 4DX']
daftar_buku_baru = daftar_buku[0:-1:2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])