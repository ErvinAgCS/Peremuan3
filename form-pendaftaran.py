print("===== Form Pendaftaran Universitas =====")
Nama = input("Masukan Nama Lengkap Anda  :")
tanggal_Lahir = input("Masukan Tanggal Lahir Anda :")
tahun_Lahir = int(input("Masukan Tahun Lahir Anda   :"))
JK = input("Masukan Jenis Kelamin Anda :")
print("========================================")
nilaia = int(input("Nilai Pelajaran Bahasa Inggris   :"))
nilaib = int(input("Nilai Pelajaran Matematika       :"))
nilaic = int(input("Nilai Pelajaran Bahasa Indonesia :"))
print("========================================")
umur = tahun_Lahir - 2024
Jumlah = nilaia + nilaib + nilaic / 3
if umur > 25 :
    if Jumlah > 80 and JK == "Laki Laki" :
        print("Anda Diterima Prodi Teknik Informatika")
    elif JK == "Perempuan" :
        print("Anda Diterima Prodi Sistem Informasi")
else :
    print("Anda Diterima Prodi DKV")
