#tipe data list
data_list =[10,11,12,13,1.4,"Faras",False]
i=0
while i <5:
    print(data_list[i]) #perulangan
    i+=1
data_list[3]="kayla" #update
print(data_list)
data_list.remove(11) #menghapus
print(data_list)
data_list.insert(3,20) #menambahkan
print(data_list)

#tipe data tuple
data_tuple =(30,40,50,60,70)
print(data_tuple, type(data_tuple))
for i in data_tuple:   #perulangan
    print(i)

#tipe data set   
data_set ={"faras",1.14, 1,True}
i=0
while i<2:
    print(data_set)#perulangan
    i+=1
data_set.discard(2)
print(data_set) #menghapus
data_set.add(50) #menambahkan
print(data_set)

#tipe data dictionary
data_dictionary ={
"asal":"malunda",
"sekolah":"SMANSA MALUNDA",
"fakultas":"teknik"}
i=0
while i<2:
    print(data_dictionary) #perulangan
    i+=2
    
data_dictionary["asal"]="majene" #update
print(data_dictionary)
data_dictionary["sekolah"]="SMA MALUNDA"
print(data_dictionary)
del data_dictionary["fakultas"] #menghapus
print(data_dictionary)
