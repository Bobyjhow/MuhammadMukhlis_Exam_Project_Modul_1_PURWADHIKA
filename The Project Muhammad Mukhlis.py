'''
Muhammad Mukhlis | Purwadhika
JC Data Science and Machine Learning
Exam Project Modul 1 : Programming Fundamental
'''

def menuread():
    while True :
        lihattdata = (input('''
Ingin Lihat Data? [1/Tekan Selain 1]
    1 --------------> Tampilkan seluruh data
    Tekan Selain 1 -> Lanjut ke cari data secara spesifik atau keluar
    Pilihan anda: '''))
        if lihattdata =='1':
            lihatdata() # line 319
            continue
        else:
            spesifik = input('''Cari Data Secara Spesifik? [1/Tekan Selain 1]
    1 --------------> Cari data secara spesifik
    Tekan Selain 1 -> Ke Menu Proceed (Exit) 
    Pilihan anda:''')
            if spesifik == '1':
                if len(listdata) == 0:
                    datakosong() # line 328
                else:
                    dataada() # line 314
                    dataspesifik = input('''\nMasukkan detail pencarian
    1 -> Berdasarkan Nama
    2 -> Berdasarkan Kelas
    3 -> Berdasarkan NISN
    Pilihan anda:''')
                    if dataspesifik == '1':
                        caridata = input('Masukkan nama yang ingin dicari: ')
                        caridata = caridata.upper()
                        templatecaridata() # line 302
                        x = 0
                        for i in range(len(listdata)):
                            if caridata == listdata[i][1]:
                                x = 1
                                print('Nomor Unik| KelaS | Nama\t| NISN       | Nilai Matematika | Nilai Fisika  | Nilai Kimia\t| Nilai Biologi ')
                                print('{}\t  | {}     | {}\t| {} | {}\t\t| {}\t\t| {}\t\t| {}'.format(i+1,listdata[i][0],listdata[i][1],listdata[i][2],listdata[i][3],listdata[i][4],listdata[i][5],listdata[i][6])) 
                        if x == 0:
                            templatedatatidakada()  # line 308     
                    elif dataspesifik == '2':
                        caridata = input('Masukkan kelas yang ingin dicari: ')
                        caridata = caridata.upper()
                        templatecaridata() # line 302
                        x = 0
                        for i in range(len(listdata)):
                            if caridata == listdata[i][0]:
                                x += 1
                                if x == 1:
                                    print('Nomor Unik| KelaS | Nama\t| NISN       | Nilai Matematika | Nilai Fisika  | Nilai Kimia\t| Nilai Biologi ')
                                print('{}\t  | {}     | {}\t| {} | {}\t\t| {}\t\t| {}\t\t| {}'.format(i+1,listdata[i][0],listdata[i][1],listdata[i][2],listdata[i][3],listdata[i][4],listdata[i][5],listdata[i][6]))
                        if x == 0:
                            templatedatatidakada() # line 308
                    elif dataspesifik == '3':
                        while True:
                            caridata = input('Masukkan NISN yang ingin dicari: ')
                            w = caridata.isnumeric()
                            if w == True:
                                w = int(caridata)
                                break
                            else :
                                templatestring() # line 296
                        templatecaridata() # line 302
                        x = 0
                        for i in range(len(listdata)):
                            if w == listdata[i][2]:
                                x += 1
                                if x == 1:
                                    print('Nomor Unik| KelaS | Nama\t| NISN       | Nilai Matematika | Nilai Fisika  | Nilai Kimia\t| Nilai Biologi ')
                                print('{}\t  | {}     | {}\t| {} | {}\t\t| {}\t\t| {}\t\t| {}'.format(i+1,listdata[i][0],listdata[i][1],listdata[i][2],listdata[i][3],listdata[i][4],listdata[i][5],listdata[i][6]))
                        if x == 0:
                            templatedatatidakada() # line 308
            else:
                yakin = input('''
Anda yakin tidak ingin mencari data? [1/Tekan Selain 1]
    1 --------------> Kembali ke Menu Utama
    Tekan Selain 1 -> Kembali ke Menu Pencarian
    Pilihan anda: ''')
                if yakin == '1':
                    break   
            continue
def menutambahdata():
    while True :
        lihatdata() # line 319
        tambahdata = (input('''Ingin tambahkan data? [1/Tekan Selain 1]
    1 --------------> Lanjut tambah data
    Tekan Selain 1 -> Ke menu proceed (Exit)
    Pilihan anda: '''))
        if tambahdata == '1':
            if len(listdata) == 0:
                nama = (input('Masukkan Nama Siswa : '))
                nama = nama.upper()
                kelas = kelasinput(1) # line 251
                nisn = nisninput(10) # line 273
                mtk = (input('Masukkan Nilai Matematika {}: '.format(nama)))
                fis = (input('Masukkan Nilai Fisika {}: '.format(nama)))
                kim = (input('Masukkan Nilai Kimia {}: '.format(nama)))
                bio = (input('Masukkan Nilai Biologi {}: '.format(nama)))
                simpan = input('''
Apakah data sudah benar dan ingin disimpan? [1/Tekan Selain 1]
    1 --------------> Simpan Data
    Tekan Selain 1 -> Kembali ke Menu Tambah Data
    Pilihan anda: ''')
                if simpan == '1':
                    listdata.append([kelas,nama,nisn,mtk,fis,kim,bio])
                    print('\nData Tersimpan\n')
                else:
                    continue
            else:
                x = 0
                nama = (input('Masukkan Nama Siswa : '))
                nama = nama.upper()
                for i in range(len(listdata)):
                    if listdata[i][1] == nama:
                        # jika nama sama
                        x = 1
                        # x menjadi 1
                    else:
                        continue
                if x == 1:
                    print('''
================================
Nama sudah ada di dalam Database
================================
''')
                else:
                    kelas = kelasinput(1) # line 251
                    nisn = nisninput(10) # line 273
                    mtk = (input('Masukkan Nilai Matematika {}: '.format(nama)))
                    fis = (input('Masukkan Nilai Fisika {}: '.format(nama)))
                    kim = (input('Masukkan Nilai Kimia {}: '.format(nama)))
                    bio = (input('Masukkan Nilai Biologi {}: '.format(nama)))
                    simpan = input('''
Apakah data sudah benar dan ingin disimpan? [1/Tekan Selain 1]
    1 --------------> Simpan Data
    Tekan Selain 1 -> Kembali ke Menu Tambah Data
    Pilihan anda: ''')
                    if simpan == '1':
                        listdata.append([kelas,nama,nisn,mtk,fis,kim,bio])
                        print('\nData Tersimpan\n')
        else:
            yakin = input('''Anda yakin tidak ingin menambahkan data? [1/Tekan Selain 1]
    1 --------------> Kembali ke Menu Utama
    Tekan Selain 1 -> Kembali ke Menu Tambah Data
    Pilihan anda: ''')
            if yakin == '1':
                break
        continue
def menuupdate():
    while True :
        if len(listdata) == 0:
            datakosong() # line 328
            break
        elif len(listdata)>0:
            dataada() # line 314
        updatedata = (input('''
Ingin update data? [1/Tekan Selain 1]
    1 --------------> Lanjut update
    Tekan Selain 1 -> Ke Menu Proceed (Exit)
    Pilihan anda: '''))
        if updatedata == '1':
            while True:
                nomorunik = input('Masukkan Nomor Unik siswa yang ingin diubah: ')
                q = nomorunik.isnumeric()
                if q == True:
                    q = int(nomorunik)
                    break
                else :
                    templatestring() # line 296
            if 1 <= q <= len(listdata):
                global j 
                j = q
                deleteupdate(j) # line 340
                updatedata = (input('''
Lanjut update data? [1/Tekan Selain 1]
    1 --------------> Lanjut ke input perubahan data
    Tekan Selain 1 -> Kembali ke Menu Update
    Pilihan anda: '''))
                if updatedata == '1':
                    datadiupdate() # line 344
                else:
                    continue
            else :
                nomoruniksalah() # line 334
                continue
        else:
            yakin = input('''
Anda yakin tidak ingin update data? [1/Tekan Selain 1]
    1 --------------> Kembali ke Menu Utama
    Tekan Selain 1 -> Kembali ke Menu Update
    Pilihan anda: ''')
            if yakin == '1': 
                break
        continue
def menudelete():
    while True :
        if len(listdata) == 0:
            datakosong() # line 328
            break
        elif len(listdata)>0:
            dataada() # line 314
        delettedata = (input('''
Ingin delete data? [1/Tekan Selain 1]
    1 --------------> Lanjut Delete
    Tekan Selain 1 -> Ke Menu Proceed (Exit)
    Pilihan anda: '''))
        if delettedata == '1':
            while True:
                nomorunik = input('Masukkan Nomor Unik siswa yang ingin dihapus: ')
                e = nomorunik.isnumeric()
                if e == True:
                    e = int(nomorunik)
                    break
                else:
                    templatestring() # line 296
            if 1 <= e <= len(listdata):
                global j
                j = e
                deleteupdate(j) # line 340
                delettedata = (input('''
Lanjut delete data? [1/Tekan Selain 1]
    1 --------------> Data akan dihapus
    Tekan Selain 1 -> Kembali ke Menu Delete
    Pilihan anda: '''))
                if delettedata == '1':
                    del listdata[j-1]
                    print('''
    =================================
    DATA YANG DIPILIH SUDAH DIHAPUS!!
    =================================
    ''')
                else :
                    continue    
            else :
                nomoruniksalah() # line 334
                continue
        else:
            yakin = input('''
Anda yakin tidak ingin mendelete data? [1/Tekan Selain 1]
    1 --------------> Kembali ke Menu Utama
    Tekan Selain 1 -> Kembali ke Menu Delete
    Pilihan anda: ''')
            if yakin == '1':
                break


        continue
def kelasinput(digit):
    while True:
        while True:
            kelas = input('Masukkan Kelas Siswa (1 Huruf A - Z): ')
            t = kelas.isnumeric() # true ketika hanya angka
            if t == False:
                break
            else:
                print('''
    =================================
         JANGAN MASUKKAN ANGKA!!!
    =================================
    ''')
        kelas = kelas.upper()
        if len(kelas) == digit:
            return kelas
        else:
            print('''
    =================================
        MASUKKAN HANYA 1 HURUF !!
    =================================
    ''')
def nisninput(digit):
    while True:
        while True:
            nisn = input('Masukkan Nomor NISN Siswa (10 Digit): ')
            r = nisn.isnumeric()
            if r == True:
                r = int(nisn)
                break
            else:
                templatestring()
        number = r
        count = 0
        while(number != 0):
            number //= 10
            count += 1
        if count == digit:
            return r
        else:
            print('''
    =================================
       MASUKKAN HANYA 10 DIGIT !!!
    =================================
    ''')
def templatestring():
    print('''
    =================================
        JANGAN MASUKKAN STRING !!
    =================================
    ''')
def templatecaridata():
    print('''
    =================================
        Berikut data yang dicari :
    =================================
    ''')
def templatedatatidakada():
    print('''
    ================================
          Data tidak ditemukan
    ================================
    ''')  
def dataada():
    print('\nDaftar Nilai Siswa\n')
    print('Nomor Unik| Kelas | Nama\t| NISN       | Nilai Matematika | Nilai Fisika  | Nilai Kimia\t| Nilai Biologi ')
    for i in range(len(listdata)) :
        print('{}\t  | {}     | {}\t| {} | {}\t\t| {}\t\t| {}\t\t| {}'.format(i+1,listdata[i][0],listdata[i][1],listdata[i][2],listdata[i][3],listdata[i][4],listdata[i][5],listdata[i][6]))
def lihatdata():
    if len(listdata) == 0:
        print('''
    ========================
        DATA MASIH KOSONG
    ========================
    ''')   
    elif len(listdata)>0:
        dataada() # line 314
def datakosong():
    print('''
    ===============================================
    DATA KOSONG!! TAMBAH DATA SISWA TERLEBIH DAHULU
    ===============================================
    ''')
def nomoruniksalah():
    print('''
    ============================================
    Nomor Unik yang dimasukkan tidak ditemukan!!
    ============================================
    ''')
def deleteupdate(j):
    print('\nDaftar Nilai Siswa\n')
    print('Nomor Unik| Kelas | Nama\t| NISN       | Nilai Matematika | Nilai Fisika  | Nilai Kimia\t| Nilai Biologi ')
    print('{}\t  | {}     | {}\t| {} | {}  \t| {}  \t| {}  \t| {}'.format(j,listdata[j-1][0],listdata[j-1][1],listdata[j-1][2],listdata[j-1][3],listdata[j-1][4],listdata[j-1][5],listdata[j-1][6])) 
def datadiupdate():
    while True:
        while True:
            kolompilih = input('''
Pilih nomor kolom yang ingin di update [KELAS = 0 / NAMA = 1 / NISN = 2 / MATEMATIKA = 3 / FISIKA = 4 / KIMIA = 5 / BIO = 6]
: ''')
            t = kolompilih.isnumeric()
            if t == True:
                t = int(kolompilih)
                break
            else:
                templatestring() # line 296
        if t == 0:
            kolombaru = kelasinput(1)
            simpan = input('''
Apakah data sudah benar dan ingin diupdate? [1/Tekan Selain 1]
    1 --------------> Data akan diubah
    Tekan Selain 1 -> Data tidak diubah
    Pilihan anda: ''')
            if simpan == '1':
                listdata[j-1][t] = kolombaru
                print('\nData Terupdate\n')
                break
            else:
                break
        elif t == 1:
            kolombaru = input('Silahkan masukkan nama baru: ')
            kolombaru = kolombaru.upper()
            simpan = input('''
Apakah data sudah benar dan ingin diupdate? [1/Tekan Selain 1]
    1 --------------> Data akan diubah
    Tekan Selain 1 -> Data tidak diubah
    Pilihan anda: ''')
            if simpan == '1':
                listdata[j-1][t] = kolombaru
                print('\nData Terupdate\n')
            else:
                break
        elif t == 2:
            kolombaru = nisninput(10)
            simpan = input('''
Apakah data sudah benar dan ingin diupdate? [1/Tekan Selain 1]
    1 --------------> Data akan diubah
    Tekan Selain 1 -> Data tidak diubah
    Pilihan anda: ''')
            if simpan == '1':
                listdata[j-1][t] = kolombaru
                print('\nData Terupdate\n')
            else:
                break
        elif t == 3:
            kolombaru = input('Silahkan masukkan nilai matematika baru: ')
            simpan = input('''
Apakah data sudah benar dan ingin diupdate? [1/Tekan Selain 1]
    1 --------------> Data akan diubah
    Tekan Selain 1 -> Data tidak diubah
    Pilihan anda: ''')
            if simpan == '1':
                listdata[j-1][t] = kolombaru
                print('\nData Terupdate\n')
            else:
                break 
        elif t == 4:
            kolombaru = input('Silahkan masukkan nilai fisika baru: ')
            simpan = input('''
Apakah data sudah benar dan ingin diupdate? [1/Tekan Selain 1]
    1 --------------> Data akan diubah
    Tekan Selain 1 -> Data tidak diubah
    Pilihan anda: ''')
            if simpan == '1':
                listdata[j-1][t] = kolombaru
                print('\nData Terupdate\n')
            else:
                break
        elif t == 5:
            kolombaru = input('Silahkan masukkan nilai kimia baru: ')
            simpan = input('''
Apakah data sudah benar dan ingin diupdate? [1/Tekan Selain 1]
    1 --------------> Data akan diubah
    Tekan Selain 1 -> Data tidak diubah
    Pilihan anda: ''')
            if simpan == '1':
                listdata[j-1][t] = kolombaru
                print('\nData Terupdate\n')
            else:
                break
        elif t == 6:
            kolombaru = input('Silahkan masukkan nilai biologi baru: ')
            simpan = input('''
Apakah data sudah benar dan ingin diupdate? [1/Tekan Selain 1]
    1 --------------> Data akan diubah
    Tekan Selain 1 -> Data tidak diubah
    Pilihan anda: ''')
            if simpan == '1':
                listdata[j-1][t] = kolombaru
                print('\nData Terupdate\n')
            else:
                break
        else:
            print('''
                =============================================
                Nomor Kolom yang dimasukkan tidak ditemukan!!
                =============================================
                ''')
            continue
        break
listdata = [] # format list = [[kelas,nama,nisn,mtk,fis,kim,bio]]
while True :
    pilihanMenu = input('''
        Selamat Datang di Database Nilai Akademik

        List Menu :
        1. Menampilkan Daftar Nilai Kelas
        2. Menambah Nilai Siswa
        3. Mengupdate Nilai Siswa
        4. Menghapus Nilai Siswa
        5. Exit Program

        Masukkan Angka Menu yang ingin dijalankan : ''')

    if(pilihanMenu ==   '1') :
        menuread() # line 7
    elif(pilihanMenu == '2') :
        menutambahdata() # line 85
    elif(pilihanMenu == '3') :
        menuupdate() # line 152
    elif(pilihanMenu == '4') :
        menudelete() # line 198
    elif(pilihanMenu == '5') :
        break
    else:
        print('''
        ==============================
        ==============================
        Masukkan pilihan dengan benar!
        ==============================
        ==============================
        ''')




