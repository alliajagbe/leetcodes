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

    def twoSum2(nums, target:int):
        right, left = 0, len(nums) - 1 
        
        pass

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
print(Solution.longestPalindrome("madam"))
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
'''
# Merge Strings Alternately
You are given two strings word1 and word2. 
Merge the strings by adding letters in alternating order, starting with word1. 
If a string is longer than the other, 
append the additional letters onto the end of the merged string.

Return the merged string.
'''
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
'''
# Greatest Common Divisor of Strings
For two strings s and t, 
we say "t divides s" if and only if s = t + ... + t 
(i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, 
return the largest string x such that x divides both str1 and str2.
'''
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
# Kids With the Greatest Number of Candies
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
# Can Place Flowers
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

#%%
'''
# Reverse Vowels of a String
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', 
and they can appear in both lower and upper cases, more than once.
'''
class Solution:
    def reverseVowels(s:str) -> str:
        vowels = "AaEeIiOoUu"

        s = list(s)

        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            
            elif s[left] not in vowels:
                left += 1
            
            elif s[right] not in vowels:
                right -= 1

        return ''.join(s)
    
print(Solution.reverseVowels("hello"))
print(Solution.reverseVowels("leetcode"))

# %%
'''
# Reverse Words in a String
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. 
The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. 
The returned string should only have a single space separating the words. 
Do not include any extra spaces.
'''
class Solution:
    def reverseWords(s:str):
        # removing whitespaces from the beginning and the end of the string
        s = s.strip()

        # turning it into a list
        s = s.split(' ')

        # removing empty strings
        for i in s:
            if i == "":
                s.remove(i)
        
        # reversing the list
        s = reversed(s)

        return ' '.join(s)
    
    def reverseWords2(s:str):
        # using list comprehension

        new_list = [char for char in reversed(s.split()) if char]

        return ' '.join(new_list)
    
print(Solution.reverseWords2("the sky is blue"))
# %%

'''
# Product of an Array Except Self
Given an integer array nums, 
return an array answer such that answer[i] is equal to the 
product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
'''

class Solution: 
    def productExceptSelf(nums):
        new_list = [1] * len(nums)

        # we first find the prefix of the list
        prefix = 1
        for i in range(len(nums)):
            new_list[i] *= prefix # we multiply the current value with the prefix
            prefix *= nums[i] # we update the prefix value by multiplying it with the current value
        
        # we do the same thing but in reverse order
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            new_list[i] *= postfix # we multiply the current value with the postfix
            postfix *= nums[i] # we update the postfix value by multiplying it with the current value
        return new_list

print(Solution.productExceptSelf([2,1,3,4]))
# %%
'''
# Increasing Triplet Subsequence
Given an integer array nums, return true if there exists a triple of indices (i, j, k) 
such that i < j < k and nums[i] < nums[j] < nums[k]. 
If no such indices exists, return false.
'''
class Solution: 
    def increasingTriplet(nums):

        # instantiating the first two smallest numbers 
        smallest = float('inf')
        second_smallest = float('inf')

        for number in nums:

            # changing the smallest number if 
            # we find a number smaller than its current value
            if number <= smallest: 
                smallest = number

            # changing the second smallest if we find 
            # a number greater than the smallest value 
            # but less than the second smallest value
            elif number <= second_smallest:
                second_smallest = number

            # if we are able to reach this point, 
            # we have been able to find three numbers
            # within our list that form the increasing
            # triplet subsequence
            else:
                return True
        
        # we return false if we dont see any subsequence
        return False
    
print(Solution.increasingTriplet([2,1,5,0,4,6]))
print(Solution.increasingTriplet([5,4,3,2,1]))
# %%
# the function below works as intended but doesnt pass the test on leetcode. 
# need to inspect why
def compress(chars):
    new_list = []

    for i in chars:
        if chars.count(i) == 1:
            new_list.append(i)
        elif i not in new_list:
            new_list.append(i)
            new_list.append(str(chars.count(i)))
    
    return new_list

compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])
# %%
