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
        answer = set()
        while n <= len(nums):
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    for k in range(j+1, len(nums)):
                        if (nums[i] + nums[j] + nums[k] == 0) and i!=j and j!=k and i!=k:
                            answer.add([nums[i], nums[j], nums[k]])
            n += 1
        
        return list(answer)


print(Solution.threeSum([-1,0,1,2,-1,-4]))
# %%

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_string = ''
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                new_string += word1[i]
            if i < len(word2):
                new_string += word2[i]

            i += 1

        return new_string