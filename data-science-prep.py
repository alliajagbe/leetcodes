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
