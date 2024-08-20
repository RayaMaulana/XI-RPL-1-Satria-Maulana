angka1 = int(input("Masukkan angka pertama: "))     # Inputkan angka1
angka2 = int(input("Masukkan angka kedua: "))       # Inputkan angka2

# operasi = input("Masukkan operator (+,-,*,/): ")  # gunakan kode ini apabila pengguna ingin menggunakan satu operator saja

class Kalkulator:
    def __init__(self, angka1, angka2) -> None:
        self.angka1 = angka1                        # Menginisialisasi atribut angka1
        self.angka2 = angka2                        # Menginisialisasi atribut angka2
    def tambah(self):                               # Membuat metode tambah
        return self.angka1 + self.angka2            # Mengembalikan hasil angka1 + angka2
    def kurang(self):                               # Membuat metode kurang
        return self.angka1 - self.angka2            # Mengembalikan hasil angka1 - angka2
    def kali(self):                                 # Membuat metode kali
        return self.angka1 * self.angka2            # Mengembalikan hasil angka1 * angka2
    def bagi(self):                                 # Membuat metode bagi
        if (angka2 != 0):                           # Mencegah error apabila angka2 = 0, yang menyebabkan error "ZeroDivisionError"
            return self.angka1 / self.angka2        # Mengembalikan hasil angka1 / angka2
        else:                   
            return "Angka Kedua tidak boleh 0"      # Akan mengembalikan hasil peringatan bahwa "Angka Kedua tidak boleh 0" apabila angka2 = 0



k = Kalkulator(angka1, angka2)                      # Membuat objek k dari class Kalkulator
print("Hasil penjumlahan:", k.tambah())             # Memberikan hasil output dari angka yang ditambahkan
print("Hasil pengurangan:", k.kurang())             # Memberikan hasil output dari angka yang dikurangkan
print("Hasil perkalian:", k.kali())                 # Memberikan hasil output dari angka yang dikalikan
print("Hasil pembagian:", k.bagi())                 # Memberikan hasil output dari angka yang dibagikan


#Ini merupakan cara lain apabila pengguna ingin menggunakan salah satu operator saja
# match operator:
#     case "+":
#         print(Kalkulator(angka1, angka2).tambah())
#     case "-":
#         print(Kalkulator(angka1, angka2).kurang())
#     case "*":
#         print(Kalkulator(angka1, angka2).kali())
#     case "/":
#         print(Kalkulator(angka1, angka2).bagi())