    

def SumOfNumbers(nums, target):
    '''
    nums : List[int]  -> List of integers with nums as variable name
    target: int -> target value ofg type int
    List[int] -> method returns a list
    '''
        
    dict = {}
    for i in range(len(nums)):
        temp = target - nums[i]
        if temp in dict:
            return [dict[temp], i]
        #dict.update({nums[i] : i})
        else:
            dict[nums[i]] = i

nums = [2,7,11,15]
target = 9
result = SumOfNumbers(nums, target)
print(result)

print("----")
nums1 = [3,2,4]
target = 6
result1 = SumOfNumbers(nums1, target)
print(result1)
