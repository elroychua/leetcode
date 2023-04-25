def topKfrequent(nums, k):
    # Notes:
    # Time: O(n) | Space: O(n)
    # Use maxheap, key of maxheap is occurence, pop from heap k times
    # Heap pop is logn
    # Bucketsort - using length of input
    #           ________________
    # Map count |0|1  |2|3|4|5|6|
    # Values       100 2 1
    # New array is bounded by 6 + 1 (proportionate to size of input array)
    # find from 6 ,5 ,4 ,3 ,2 ,1
    # Top K [1, 2]
    # HashMap is used to count occurences of each value
    count = {}
    # list of values that occur n times.
    freq = [[] for i in range(len(nums)+1)]
    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)
    res = []
    # decrement
    for i in range(len(freq) - 1, 0, -1):
        # sublist in freq, could be empty or not.
        for n in freq[i]:
            # append if nonempty
            res.append(n)
            # once len of res is same as k, return res
            if len(res) == k:
                return res
# Time: O(klogn) | Space: O(klogn)
# Bucket Sort


# Test cases
print("Test Cases for top k frequent elements: ")
nums1 = [1, 1, 1, 2, 2, 3]
k1 = 2
print(topKfrequent(nums1, k1))
nums2 = [1]
k2 = 1
print(topKfrequent(nums2, k2))
