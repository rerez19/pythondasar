import pandas as pd

# String of vowels
vowels = 'aeiou'

# Input dari pengguna
ip_str = input("Masukkan sebuah kalimat: ")

# Modifikasi kalimat agar memiliki format yang sama setiap karakter
ip_str = ip_str.casefold()

# Membuat sebuah dictionary dengan setiap huruf vokal menjadi key dan value
count = {}.fromkeys(vowels, 0)

# Menghitung jumlah huruf vokal
for char in ip_str:
    if char in count:
        count[char] += 1

# Membuat dataframe dari dictionary
count_table = pd.DataFrame(count, index=['Jumlah'])
print(count_table)
