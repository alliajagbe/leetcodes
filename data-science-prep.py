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

    if len(x) < 3:
        return None
    
    elif len(x) == 3:
        return x[0] * x[1] * x[2]
    
    else:
        # getting the first three maximum positive numbers
        positives = [i for i in x if i > 0]
        first_three = sorted(positives, reverse=True)[:3]

        # if there are negative numbers in the array
        negatives = [i for i in x if i < 0]

        if len(negatives) == len(x): # all the numbers in the array are negative
            first_three = sorted(negatives, reverse=True)
            return first_three[0] * first_three[1] * first_three[2]
        else:
            first_two = sorted(negatives)[:2]

        return max(first_three[0]*first_three[1]*first_three[2], first_three[0]*first_two[0]*first_two[1])

maxProduct([-2,-6,1,3, 2])

# %%
'''
Given an integer array, find the sum of the largest 
contiguous subarray within the array. 
For example, given the array A = [0,-1,-5,-2,3,14] 
it should return 17 because of [3,14]. 
Note that if all the elements are negative it should return zero.
'''
def largestSum(x):
    
    max_sum = current_sum = 0
    for i in x: 
        current_sum += i
        if current_sum < 0: 
            current_sum = 0
        
        max_sum = max(max_sum, current_sum)

    if max_sum > 0:
        return max_sum
    else:
        return 0
    
largestSum([-1,4,-2,6,-6,2,-3])

# %%
'''
Given an integer n and an integer K, 
output a list of all of the combinations 
of k numbers chosen from 1 to n. 
For example, if n=3 and k=2, return [1,2],[1,3],[2,3]
'''
def combinations(n, k):
    from itertools import combinations
    final_list = []

    # creating a list of all the possible combinations of k numbers from 1 to n
    comb = combinations([i for i in range(1, n+1)], k)

    for i in comb: 
        final_list.append(i)

    return final_list

combinations(3, 2)

# %%
'''
Write a function to generate N samples 
from a normal distribution and plot them on 
the histogram
'''
def normalDistribution(n):
    import matplotlib.pyplot as plt
    import numpy as np

    numbers = np.random.randn(n)

    # plotting a histogram
    plt.hist(numbers, bins=20)
    plt.ylabel("Frequency")
    plt.xlabel("Numbers")
    plt.show()

normalDistribution(1000)

# %%
