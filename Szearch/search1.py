#순차검색
def Re_search(array,key):
    i=0
    while(i < len(array) ):
        if (key == array[i]):
            return array[i],i
        else:
            i +=1
    return "can't find"


def Re_insert(arr,key,idx):
    arr.append(key)
    for i in range(len(arr)-idx-1):
        arr[len(arr)-1-i] = arr[len(arr)-2-i]
    arr[idx]=key
    return arr

def Re_delete(array,key):
    value,idx = Re_search(array,key)
    array[idx] = None
    return arr

    

arr=[1,2,3,4,5,6,7,8,9]
arr = Re_insert(arr,1.5,1)
arr =  Re_delete(arr,7)
print(arr)


