from collections import defaultdict


def groupAnagrams(strs):
    # Time: O(m * n log n) | Space: O(m * n log n)
    # array count [] count chars from a -z, how many each char.
    res = defaultdict(list)
    for str in strs:
        count = [0] * 26
        for c in str:
            count[ord(c) - ord("a")] += 1
        res[tuple(count)].append(str)
    return res.values()


# Test Cases
print("Test Cases for group anagrams: ")
case_1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(case_1))
case_2 = [""]
print(groupAnagrams(case_2))
case_3 = ["a"]
print(groupAnagrams(case_3))
