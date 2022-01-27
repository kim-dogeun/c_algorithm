def select_sort(arr):
    sorted = []
    for j in range(len(arr)):
        min = 100
        for i in range(len(arr)):
            if (arr[i]<min):
                min = arr[i]
                minindex = i
        arr.pop(minindex)
        sorted.append(min)
    print(sorted)
        
arr= [1,0,5,8,9,4,3,6,6,8,7,7,2]
select_sort(arr)


def insert_sort(arr):
    for i in range(len(arr)):
        j=i
        while(arr[j-1]>arr[i] and j>0):
            arr[j]=arr[j-1]
            j=j-1
        arr[j] = arr[i]
    return arr

arr= [1,0,5,8,9,4,3,6,6,8,7,7,2]
arr = select_sort(arr)

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            while(arr[j]>arr[j+1]):
                k= arr[j+1]
                arr[j+1] = arr[j]
                arr[j]=k           
    return(arr)

arr= [1,0,5,8,9,4,3,6,6,8,7,7,2]
asd = bubble_sort(arr)
print(asd)