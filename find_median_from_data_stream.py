'''
Problem: https://leetcode.com/problems/find-median-from-data-stream/
'''
from heapq import *

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxheap = []
        self.minheap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        # Item being added at the odd'th position goes into min heap
        
        if len(self.maxheap) == len(self.minheap):
            heappush(self.minheap, -heappushpop(self.maxheap, -num))
            
        else:
            heappush(self.maxheap, -heappushpop(self.minheap, num))
        
    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.maxheap) == len(self.minheap):
            return (-self.maxheap[0] + self.minheap[0])/2.0
        return self.minheap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
