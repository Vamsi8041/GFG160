class Solution:
    #Function to rotate an array by d elements 
    def rotateArr(self, arr, d):
        #Your code here
        d=d%len(arr)
        arr[:]=arr[d:]+arr[:d]
        return arr