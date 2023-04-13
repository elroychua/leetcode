def twoSum(nums, target):
    #Time: O(n)^2 | Space: O(n)^2
    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return [i, j]
    # return [0, 0]
    #Time: O(n) | Space: O(n)
    map_nums = {}
    for i, n in enumerate(nums): 
    # enumerate returns a tuple (index, value) i is index, n is value
        if target - n in map_nums:
            # if the difference between target and n is in the map
            # then we have found the pair
            return [map_nums[target - n], i]
        else:
            # if the difference is not in the map, then we add the value
            map_nums[n] = i
    # if we don't find a pair, we return [0, 0]
    return [0, 0]
#difference from O(n)^2 and O(n) saves 20ms per function call
print("Test Cases for two sum: ")
case_1 = [2, 7, 11, 15]
target_1 = 9
case_2 = [3, 2, 4]
target_2 = 6
case_3 = [3,3]
target_3 = 6

print(twoSum(case_1, target_1))
print(twoSum(case_2, target_2))
print(twoSum(case_3, target_3))
