from collections import defaultdict


def groupAnagrams(strs):
    # Time: O(m * n log n) | Space: O(m * n log n)
    # array count [] count chars from a -z, how many each char.
    res = defaultdict(list)
    for s in strs:
        count = [0] * 26  # set array to 26 0's
        for c in s:  # for each char in string
            count[ord(c)-ord("a")] += 1  # gives 0-25
        # after for loop, count will hold the number of each char
        res[tuple(count)].append(s)
        # tuple(count) is the key, s is the value
    return res.values()


# Test Cases
print("Test Cases for group anagrams: ")
case_1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(case_1))
case_2 = [""]
print(groupAnagrams(case_2))
case_3 = ["a"]
print(groupAnagrams(case_3))
