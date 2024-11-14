def prima(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

while True:
    angka = int(input("Masukkan angka): "))
    if angka == 'Enter':
        break
    if prima(int(angka)):
        print("Adalah bilangan prima")
    else:
        print("Bukan bilangan prima")
10