nums = [2,8,5,4,9]
class Solution:
    def sortArray(self, nums):
       for i in range(len(nums)):
           for j in range(i+1, len(nums)):
               if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

solution = Solution()
solution.sortArray(nums)
print(nums)

# arrs = input("Enter the Elements of Array:")
# arr = [int(num) for num in arrs.split(',')]
# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i] > arr[j]:
#             arr[i], arr[j] = arr[j], arr[i]
# print(arr)