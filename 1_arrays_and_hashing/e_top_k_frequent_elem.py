def topKfrequent(nums, k):
    # Time: O(m * n log n) | Space: O(m * n log n)
    # Bucketsort - using length of input
    count = {}
    freq = [[] for i in range(len(nums)+1)]
    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)
    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res


# Test cases
print("Test Cases for top k frequent elements: ")
nums1 = [1, 1, 1, 2, 2, 3]
k1 = 2
print(topKfrequent(nums1, k1))
nums2 = [1]
k2 = 1
print(topKfrequent(nums2, k2))
