#%%
'''
Given two arrays, write a python function to return the intersection of the two. 
For example, X = [1,5,9,0] and Y = [3,0,2,9], it should return [9,0].
'''
def intersection(x,y):
    return list(set(x).intersection(set(y)))

# function test
intersection([1,5,9,0],[3,0,2,9])
# %%

'''
Given an array, find all the duplicates in the array.
For example, input: [1,2,3,1,3,6,5], output: [1,3]
'''
def duplicates(x):
    return list(set([i for i in x if x.count(i) > 1]))

# function test
duplicates([1,2,3,1,3,6,5])

# %%
'''
Given an integer array, return the maximum product of any 
three numbers in the array.
'''
def maxProduct(x):
    # getting the first three maximum positive numbers
    positives = [i for i in x if i > 0]
    first_three = sorted(positives)[-3:]

    # if there are negative numbers in the array
    negatives = [i for i in x if i < 0]
    first_two = sorted(negatives)[:2]
    return max(first_three[0]*first_three[1]*first_three[2], first_three[0]*first_two[0]*first_two[1])

maxProduct([2,6,3,1,5,7,8])

# %%
