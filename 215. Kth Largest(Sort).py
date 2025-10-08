class Solution:
    def kthLargest(self, arr, k):
        if len(arr) == 1:
            return arr[0]

        arr = arr[::-1]
        print(arr)
        return arr[k-1]


solution = Solution()
N = 5
arr = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k= 4
result = solution.kthLargest(arr, k)
print("The kth Largest Element is:",result)