def counterClockwise(val):           # Membuat sebuah function dengan nama counterClockwise dengan satu parameter yaitu val 
    L=[]                             # empty list
    for i in range(len(val)):        # looping i in range(0,3)
        if type(val[i])==list:       # jika tipe data berupa list
            for item in val[i]:      # maka untuk setiap item di dalam list tersebut
                L.append(item)       # akan di-append ke dalam L

    tukar1=L[2::3]                     # slicing list dari index ke 2 -->3 dengan step 3
    tukar2=L[1::3]                     # slicing list dari index ke 1 -->2 dengan step 3
    tukar3=L[::3]                      # slicing list dari index ke 0 -->1 dengan step 3
    data_mutar=[tukar1, tukar2, tukar3]      # list akan digabung menjadi satu dalam sebuah list bernama data_mutar
    return data_mutar                       #  return data_mutar


list_awal = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]   # list dalam sebuah list
print(counterClockwise(list_awal))            # print function 