def contains_duplicate(nums):
    # Time: O(n)^2 | Space: O(n)^2
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False
    # Time: O(n) | Space: O(n)
    # set_nums = set()
    # for n in nums:
    #     if n in set_nums:
    #         return True
    #     set_nums.add(n)
    # return False
print("Test Cases for contains duplicate: ")
case_1 = [1,2,3,1]
case_2 = [1,2,3,4]
case_3 = [1,1,1,3,3,4,3,2,4,2]

print(contains_duplicate(case_1))
print(contains_duplicate(case_2))
print(contains_duplicate(case_3))

