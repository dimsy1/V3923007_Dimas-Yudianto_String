nama = input("Masukkan Nama Anda: ").lower()

vokal = "aiueo"
konsonan = "bcdfghjklmnpqrstvwxyz"

jumlahHuruf = 0
jumlahVokal = 0
jumlahKonsonan = 0

for x in nama:
    if x != " ":
        jumlahHuruf += 1

for x in nama:
    if x in vokal:
        jumlahVokal += 1

for x in nama:
    if x in konsonan:
        jumlahKonsonan += 1

print("Jumlah huruf dari nama Anda adalah " + str(jumlahHuruf))
print("Jumlah huruf vokal dari nama Anda adalah " + str(jumlahVokal))
print("Jumlah huruf konsonan dari nama Anda adalah " + str(jumlahKonsonan))