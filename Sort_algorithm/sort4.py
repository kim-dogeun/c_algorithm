def mergesort(left,right):
    new=[]
    while (len(left)>0 or len(right)>0):
        if len(left) == 0:
            new.append(right[0])
            del right[0]
        if len(right) == 0:
            new.append(left[0])
            del left[0]
        if len(left) != 0 and len(right) != 0:
            if left[0] >= right[0]:
                new.append(right[0])
                del right[0]
            else:
                new.append(left[0])
                del left[0]
    return new

left=[1,3,5,6,7,8,9]
right = [2,3,4,5,7,8]
a=mergesort(left,right)
print(a)

def merge(arr):
    if(len(arr)<=1):
        return arr
                    
    mid_index=len(arr)//2
    left=arr[0:mid_index]
    right=arr[mid_index:]
    left1=merge(left)
    right1=merge(right)
    return mergesort(left1,right1)

    
arr= [1,0,5,8,9,4,3,6,6,8,7,7,2]
asd = merge(arr)
print(asd)

