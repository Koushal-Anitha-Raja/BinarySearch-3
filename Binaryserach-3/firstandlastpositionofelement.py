class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        #declaring the variables outside
        self.nums=nums
        self.target=target
        #initializing the flag value for first time as true
        first=self.binarySearch(True)
        last=self.binarySearch(False)
        
        return[first,last]
        
    def binarySearch(self,LeftFlag):
        
        #initialize i as -1 because if its not found return -1
        index=-1
        
        #assigning low value to zero
        l=0
        #assigning high value to last value (here one less then length as index starts from 0)
        h=len(self.nums)-1
         
        #continue until low is less than or equal high
        while l<=h:
            #finding the mid value with integer overflow check
            mid=l+(h-l)//2
            
            
            #if the first time the element is found
            if self.nums[mid]== self.target:
                index=mid
                #if the index is found 
                  #if the leftflag value changed 
                if LeftFlag:
                    h=mid-1
            
                else:
                    l=mid+1
                
            #if the mid elemnt is less than target    
            if self.nums[mid]< self.target:
                l=mid+1
    
            #if the mid element is greater than target    
            if self.nums[mid]> self.target: 
                h=mid-1
                
      
            
        return index     