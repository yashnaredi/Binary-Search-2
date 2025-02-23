# Binary-Search-2

## Problem 1: (https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
#time complexity:O(log n)
#space complexity:O(1)
#leetcode solution accepted
# the easiest approach to this problem is to perform two sepearte binary search on two havles of the array
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
    #performing the search on left side or low side 
        def searchleft(nums,target):
            #intializing index 
            index=-1
            #basic binary search
            #but instead of returning the element we are setting the index to that point
            left =0
            right= len(nums)-1
            while(left<=right):
                mid =(left+right)//2
                if nums[mid]>=target:
                    right = mid-1
                else:
                    left =mid+1
                if nums[mid]==target:
                    index = mid
            return index
        
        #performing binary search on high side same as on the left side
        def searchright(nums,target):
            index=-1
            left =0
            right= len(nums)-1
            while(left<=right):
                mid =(left+right)//2
                if nums[mid]<=target:
                    left = mid+1
                else:
                    right = mid-1
                if nums[mid]==target:
                    index = mid
            return index
        #calling the index from left search and rigght search at 0and 1 postion respectively
        result = [-1,-1]
        result[0]=searchleft(nums,target)
        result[1]=searchright(nums,target)
        return result

    
    
    
    
    
    
   