#%%

def longestCommonPrefix(strs) -> str:
    if len(strs) == 0:
        return ""
    elif len(strs) == 1:
        return strs[0]
    else:
        shortest_word = min(strs, key=len)
        print("shortest word",shortest_word)
        i = 1
        while i <= len(shortest_word):
            for element in strs:
                # temp = shortest_word[:i]
                if shortest_word[:i] != element[:i]:
                    return shortest_word[:i]
            
            i += 1

print(longestCommonPrefix(["ab","a"]))

#%%