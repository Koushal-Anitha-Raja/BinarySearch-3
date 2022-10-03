def FindMissingNumber(arr):
    #assigning low value to zero
    l=0
    #assigning high value to last value (here one less then length as index starts from 0)                
    h=len(arr)-1
    
    #if the first element is missing
    if arr[0]!=1:
        return 1
    
    #if the last element is missing
    if arr[-1]==len(arr):
        return len(arr)+1
    
    
    #checking whether the low plus one is equal to high     
    while(l+1!=h):
         #finding the mid value with integer overflow check
            mid=l+(h-l)//2
            
        
        #if index and value of mid are same 
            if arr[mid]-mid==1:
            #move the low pointer to mid
                l=mid
            else:
            #move the high pointer to mid
                h=mid
            
    return  arr[l]+1        
        
print(FindMissingNumber([1,2,3,5,6,7]))