#%%
# Finding longest common prefix

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
            else:
                return -1

print(Solution.search([-1,0,3,5,9,12], 9))
# %%
