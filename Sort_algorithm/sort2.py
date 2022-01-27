
#퀵정렬 틀린건 알겠는데 어디를 고칠지 모르겠다.... 새로하는게 나을듯

def quick_sort(arr):
    i=0
    j=len(arr)-1
    if (j>0):
        line = arr[-1]
    else:
        return

    key1 = None
    key2 = None
    running = True
    while(running):
        while(i < j):
            if(arr[i] > line):
                key1=arr[i]
            else:
                i=i+1

            if(arr[j] < line):
                key2=arr[j]
            else:
                j=j-1
            
            temp = key2
            key2 = key1
            key1=temp

            if(i==j):
                running=False
            

        temp2 = arr[-1]
        arr[-1] = arr[i]
        arr[i] = temp2
        arr1 = arr[0:i]
        arr2 = arr[i+1:]
        
        
        quick_sort(arr1)
        quick_sort(arr2)

arr= [1,0,5,8,9,4,3,6,6,8,7,7,2]
asd = quick_sort(arr)
print(asd)




