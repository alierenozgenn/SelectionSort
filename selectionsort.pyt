def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Minimum elemanın indeksini bulun
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Bulunan minimum elemanı ilk elemanla yer değiştirin
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
        # Her adımda dizinin durumunu yazdırın
        print(f"Adım {i+1}: {arr}")
    
    return arr

# Kullanıcıdan girdi al
input_string = input("Diziyi virgülle ayrılmış şekilde girin: ")
array = [int(x) for x in input_string.split(",")]

# Sıralamayı yap ve sonucu göster
sorted_array = selection_sort(array)
print("Sonuç:", sorted_array)
