suma = 0
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
        suma = suma + i

print(f'Suma de números pares: {suma}')