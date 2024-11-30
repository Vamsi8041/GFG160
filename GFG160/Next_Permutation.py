class Solution:
    def nextPermutation(self, arr):
        n=len(arr)
        
        pivot=-1
        for i in range(n-2,-1,-1):
            if arr[i]<arr[i+1]:
                pivot=i
                break
        
        if pivot==-1:
            return arr.reverse()
        else:
            for i in range(n-1,pivot,-1):
                if arr[i]>arr[pivot]:
                    arr[i],arr[pivot]=arr[pivot],arr[i]
                    break
            left=pivot+1
            right=n-1
            for i in range((n-pivot)//2):
                arr[left],arr[right]=arr[right],arr[left]
                left+=1
                right-=1
            
            return arr