pilihan= 0
nilai= ["bola","sepatu"]
while pilihan <= 1:
    print ("selesai")
    print ("1. mencetak list")
    print ("2. Menambahkam nama ke dalam list")
    print ("3. Menghapus nama dari list")
    print ("4. Mengubah data dalam list")
    print ("5. Menampilkan index barang tertentu")
    print ("6. Mengetahui apakah barang sudah ada di dalam list atau belum")
    print ("9. keluar")
    menu_item = int(input("pilih menu: "))
    if menu_item == 1:
        current = 0
        if len(nilai) > 0:
              while current < len(nilai):
                print (current, ".", nilai[current])
                current = current + 1
        else:
              print ("list kosong")

    elif menu_item == 2 : 
            name = input("Masukkan nilai: ")
            nilai.append(name)
            print(nilai)
    elif menu_item == 3:
        del_name = input("nilai yang ingin di hapus: ")
        if del_name in nilai:
#namelist.remove(del_name) dapat di gunakan
            item_number = nilai.index(del_name)
            del nilai[item_number]
            print(nilai)
#kode di atas hanya menghapus nama pertama yang ada
#kode di bawah ini menghapus semua nama
#while del_name in namelist:
#item_number = namalist.index(del_name)
#del namelist[item_number]
        else:
             print (del_nilai, "tidak di temukan")
    elif menu_item == 4:
        old_name = input("Nama apa yang ingin di ubah")
        if old_name in nilai:
            item_number = nilai.index(old_name)
            new_name = input("nama baru: ")
            nilai[item_number] = new_name
            print(nilai)
        else:
              print (old_name, "tidak di temukan")

    elif menu_item == 5:
         print(nilai)
         nilai_yang_ingin_dicari = input("masukan nilai yang di cari :")
         print(nilai_yang_ingin_dicari,"berada pada index",nilai.index(nilai_yang_ingin_dicari))

    elif menu_item == 6:
        nilai_yang_ingin_dicari = input("masukkan nilai  yang ingin di cari :")
        if nilai_yang_ingin_dicari in nilai:
            print("nilai ini terdapat dalam nilai")
        elif nilai_yang_ingin_dicari not in nilai :
            print("nilai ini tidak terdapat dalam nilai")
            

   
        
        
            
              
              
