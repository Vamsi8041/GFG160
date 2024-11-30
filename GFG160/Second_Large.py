#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        second=float('-inf')
        max_ele=float('-inf')
        
        for i in range(len(arr)):
            if arr[i]>max_ele:
                second=max_ele
                max_ele=arr[i]
            elif arr[i]>second and arr[i]!=max_ele:
                second=arr[i]
        if second==float('-inf'):
            return -1
        else:
            return second