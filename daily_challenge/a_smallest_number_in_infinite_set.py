class smallestInifinteSet(object):

    def __init__(self):
        self.seen = [False] * 1005

    def popSmallest(self):
        for i in range(1, 1005):
            if not self.seen[i]:
                self.seen[i] = True
                return i

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
