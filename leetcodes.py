#%%
# Finding Longest Common Prefix from an Array of Strings

def longestCommonPrefix(strs) -> str:
    if len(strs) == 0:
        return ""
    elif len(strs) == 1:
        return strs[0]
    else:
        temp = strs[0]
        for element in strs[1:]:
            while len(temp) > 0:
                if element.startswith(temp) == False:
                    temp = temp[:-1]
                else: 
                    break
        return temp

print(longestCommonPrefix(["ab","a"]))

# %%
# Binary Search on Sorted Arrays
class Solution:
    def search(nums, target: int) -> int:
        high = len(nums) - 1
        low = 0
        while low <= high:
            mid = (high+low)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
        return -1

print(Solution.search([-1,0,3,5,9,12], 9))
# %%

# Two Sums
'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

class Solution:
    def twoSum(nums, target: int):
        print(sum(nums))
        for i,j in zip(nums,nums):
            if (i + j == target):
                return [nums.index(i),nums.index(j)]

print(Solution.twoSum([2,7,11,15],9))
        

# %%
