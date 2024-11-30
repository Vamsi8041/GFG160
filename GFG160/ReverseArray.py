class Solution:
    def reverseArray(self, arr):
        # code here
        last=len(arr)-1
        for i in range(len(arr)//2):
            arr[i],arr[last]=arr[last],arr[i]
            last-=1
        return arr