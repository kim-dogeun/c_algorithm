def di_search(key,array):
    left = 0
    right= len(array)
    while(left < right):
        mid = int((left + right +1)/2)
        if left+1 == right:
            if key == array[left]:
                return array[left], left
            else:
                print('key값 존재하지 않음')
                return array[left], left
        if key == array[mid]:
            return array[mid], mid 
        elif key < array[mid]:
            right = mid
        elif key > array[mid]:
            left = mid
        
arr = [1,3,5,6,7,9,10,12,14,16,17,19]

def di_insert(key,array):
    before_key, before_idx = di_search(key,array)
    array.append(key)
    for i in range(len(arr)-1-before_idx):
        array[len(arr)-i-1] = array[len(arr)-i-2]
    array[before_idx+1] = key
    
    return array    

print(di_insert(20,arr))

