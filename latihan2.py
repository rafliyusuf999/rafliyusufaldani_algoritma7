def add_ordinal_suffix(number):
    if 10 <= number % 100 <= 20:
        return f"{number}th"
    suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(number % 10, 'th')
    return f"{number}{suffix}"

n = int(input("Masukkan jumlah input: "))
for _ in range(n):
    number = int(input(">>"))
    if number == 0:
        print("0th\nbye bye :3")
        break
    print(add_ordinal_suffix(number))
