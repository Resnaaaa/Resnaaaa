#1. menggabungkan string dan angka dengan operator koma.
print('Hello',12) # Hello 12
print('=========================================')

# 2. Menggunakan operator * dan +
print('Hello' * 5) # akan menduplicate string Hello sebanyak 5 kali
print(15 * 18) # akan mengalikan bilangan tersebut
print('=========================================')

print('Hello' + 'World') # akan menggabungkan kedua string tersebut
print(18 + 25) # akan menambahkan kedua bilangan tersebut
print('=========================================')

#Output
# HelloHelloHelloHelloHello
# 270
# Hello World
# 43

# 3. Mengetahui Tipe data menggunakan func type()
print(type('hello')) # output : <class 'str'>
print(type(50 + 10j)) # output : <class 'complex'>
print('=========================================')

# 4. Parsing String to other data types or change all data types
print(int('100') / 4) # output : 25
print('i like ejen ali season ' + str(3)) # output : i like ejen ali season 3 
print('=========================================')
a = None
print(type(a))

print('Halo nama saya ' + str(20) * 3)
print('=========================================')

# 5. String Indexing

print('Hello'[0])
print('Hello'[3])
print('=========================================')

print('Hello'[-1])  # Negative Index
print('=========================================')
"""Jika ingin mendapatkan character dihitung dari akhir dari sebuah string,
maka kita dapat menggunakan tanda - dan dimulai dari indeks 1 untuk mendapatkan character terakhir dari string."""

# 6.String Built-In Function
teks= 'Halo,Kami NG"
# Split function -> Digunakan untuk memisahkan string sesuai dengan separator yang kita inginkan dan mengembalikan hasilnya sebagai sebuah list.
x = teks.split(',  ')
print(x)
print('=========================================')

a = "Halo"
b = "halo"
# islower() function -> Digunakan untuk mengecek apakah semua element dalam string adalah huruf kecil, akan mengembalikan True jika iya, dan False jika tidak
print(b.islower())
print(a.islower())
print('=========================================')

# count() function -> Digunakan untuk menghitung berapa kali sebuah value muncul dalam sebuah string
teks = "Halo semuanya, kami mengerjakan ini setelah ujian di sekolah,pusingnyooo"
x = teks.count("semuanya")
print(x)
print('=========================================')

# 7. Built-in function

# Tipe data integer
x = int("17")
y = int(17.5)

print(x)
print(y)
print('=========================================')
# output
# 17
# 17

# Tipe data float:
# pow() -> Digunakan untuk mendapatkan nilai pangkat dari suatu bilangan. Contohnya:
x = pow(3, 3) # 5 pangkat 3
y = pow(5, -3) # 5 pangkat -3

print(x)
print(y)
print('=========================================')
#output
# 125
# 0.008

# Tipe data string
# str() -> Digunakan untuk mengubah sebuah objek menjadi string. Contohnya:
x = str(12)
y = str(12.5)

print(type(x))
print(type(y))
print('=========================================')
#output
# <class 'str'>
# <class 'str'>
