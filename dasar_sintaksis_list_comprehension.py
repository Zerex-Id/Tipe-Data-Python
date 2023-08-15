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