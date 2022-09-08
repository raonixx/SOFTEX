def insertionSort(array):

    for step in range(1,len(array)):
        key = array[step]
        j = step - 1

        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j = j - 1


        array[j + 1] = key

data = [45, 41, 39, 23, 15, 9, 27, 43, 17, 11, 5, 25, 43, 13]
insertionSort(data)
print('Array em ordem crescente: ')
print(data)
