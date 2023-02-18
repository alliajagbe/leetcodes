#%%

def longestCommonPrefix(strs) -> str:
    shortest_word = min(strs, key=len)
    print("shortest word",shortest_word)
    i = 1
    while i <= len(shortest_word):
        for element in strs:
            # temp = shortest_word[:i]
            if shortest_word[:i] == element[:i]:
                continue
            else:
                return ""
        
        i += 1
    final_prefix = shortest_word[:i]
    print(final_prefix)

    return final_prefix

longestCommonPrefix(["flower","flow","flight"])

#%%