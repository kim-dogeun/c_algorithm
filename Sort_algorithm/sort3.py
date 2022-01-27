#힙정렬

def upheep(arr,k):
    key = arr[k]
    while(arr[k//2] < key):
        arr[k] = arr[k//2]
        k=k//2
        arr[k] = key

def down(arr,k):
    key = arr[k]
    while(k<len(arr)//2):
        i = k*2
        while(i>0 and i<len(arr)):
            if(i< len(arr)-1 and arr[i]<arr[i+1]):
                i +=1
            if(i< len(arr)-1 and key<arr[i]):
                arr[k]=arr[i]
                arr[i] = key
                k=i
            if(key>=arr[i]):
                break
        
def insert(arr,newkey):
    arr.append(newkey)
    upheep(arr,len(arr)-1)

def extract(arr):
    maxvalue = arr[1]
    arr[1] = arr[-1]
    del arr[-1]
    down(arr,1)
    return maxvalue

def hip_sort(arr):
    sorted1=[]
    sorted2=[]
    for i in range(len(arr)):
       insert(sorted1,i)
    for i in range(len(sorted1)):
       k = extract(sorted1)  
       sorted2.append(k)
    return sorted2

arr= [1,0,5,8,9,4,3,6,6,8,7,7,2]
asd = hip_sort(arr)
print(asd)

