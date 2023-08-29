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
    def mergeAlternately(word1: str, word2: str) -> str:
        new_string = ''
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                new_string += word1[i]
            if i < len(word2):
                new_string += word2[i]

            i += 1

        return new_string
    
    def mergeAlternately2(word1: str, word2: str) -> str:
        # getting the minimum length of the two strings
        minimum = min(len(word1), len(word2))

        # new string to be formed
        new_string = ''

        for i in range(minimum):
            new_string += word1[i] + word2[i]
        
        # adding the rest of the letters 
        new_string += word1[minimum:] + word2[minimum:]

        return new_string
    
print(Solution.mergeAlternately("ab", "pqrs"))
print(Solution.mergeAlternately2("ab", "pqrs"))
# %%
class Solution:
    def gcdOfStrings(str1: str, str2: str) -> str:

        if str1 + str2 != str2 + str1: 
            answer = ""
        else:
            # function to find the greatest common divisor of two numbers
            def gcd(a,b):
                while b:
                    # we keep swapping so that a is always the bigger number
                    # and b is the smaller one
                    # we are basically finding the remainder iteratively until the 
                    # remainder is zero
                    a,b = b, a%b
                return a
            answer = str1[:gcd(len(str1), len(str2))]
        return answer
    
print(Solution.gcdOfStrings("ABCABC", "ABC"))
# %%
'''
There are n kids with candies. 
You are given an integer array candies, 
where each candies[i] represents the number of candies the ith kid has, 
and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, 
where result[i] is true if, after giving the ith kid all the extraCandies, 
they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.
'''
class Solution:
    def kidsWithCandies(candies, extraCandies: int):
        # we define a function to give the maximum number of candies a kid has in the list
        def maximum(candies):
            max_candy = 0
            for i in range(len(candies)):
                if candies[i] > max_candy:
                    max_candy = candies[i]
                else:
                    continue
            return max_candy
        
        # using list comprehension, we find all the list of all booleans returning true or false
        # if with the addition of the extra candies, they get more than the maximum number of candies
        # in the list
        boolean_array = [candy + extraCandies >= maximum(candies) for candy in candies]
        return boolean_array
    
print(Solution.kidsWithCandies([2,3,5,1,3], 3))

#%%

'''
You have a long flowerbed in which some of the plots are planted, and some are not. 
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, 
where 0 means empty and 1 means not empty, and an integer n, 
return true if n new flowers can be planted in the flowerbed 
without violating the no-adjacent-flowers rule and false otherwise.
'''
class Solution:
    def canPlaceFlowers(flowerbed, n: int) -> bool:
        if n == 0:
            return True
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i==0 or flowerbed[i-1]==0) and (i==len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1

            if n == 0:
                return True
        
        return False
    
print(Solution.canPlaceFlowers([1,0,0,0,1],1))

# %%
