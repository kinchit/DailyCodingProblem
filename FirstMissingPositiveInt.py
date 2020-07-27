'''
This problem was asked by Stripe.
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
You can modify the input array in-place.
'''

def MissingInteger(L):
    L.sort()
    num = 0
    for i in range(len(L)-1):
        if L[i+1] - L[i] > 1:
            num = L[i+1] - L[i]
    if num == 0 and L[i+1] == L[-1]:
        num = L[i+1] + 1
    print(num)
  
# def getMissingNo(L): 
#     n = len(L) 
#     total = (n + 1)*(n + 2)/2
#     sum_of_L = sum(L) 
#     return total - sum_of_L
    
    
L = [3, 4, -1, 1]
L2 = [1, 2, 0]
MissingInteger(L)
#print(getMissingNo(L))