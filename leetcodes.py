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

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution:
    def twoSum(nums, target: int):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i]+nums[j]) == target:
                    return [i,j]
                else:
                    continue

print(Solution.twoSum([3,3],6))
        

# %%
# Longest Palindromic Substring

# Given a string s, return the longest palindromic substring in s.

class Solution:
    def longestPalindrome(s: str) -> str:
        palindrome = '' 
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                if len(palindrome) >= j-i:
                    break
                elif s[i:j] == s[i:j][::-1]:
                    palindrome = s[i:j]
                    break
        return palindrome

print(Solution.longestPalindrome("pneumonoultramicroscopicsilicovolcanoconiosis"))
# %%

class Solution:
    def threeSum(nums):
        n = 0
        answer = []
        while n <= len(nums):
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    for k in range(j+1, len(nums)):
                        if (nums[i] + nums[j] + nums[k] == 0):
                            answer.append([nums[i], nums[j], nums[k]])
            n += 1


print(Solution.threeSum([-1,0,1,2,-1,-4]))
# %%
