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
    return [i for i in x if x.count(i) > 1]
