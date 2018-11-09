'''
Problem: https://leetcode.com/problems/kth-largest-element-in-a-stream
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, which contains initial elements from the stream. For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.

Example:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
'''
class KthLargest:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.num = nums
        self.k = k
        
        # num items satisfies min heap property
        heapq.heapify(self.num)
        
        # Store only the k largest elements 
        while(len(self.num) > k):
            heapq.heappop(self.num)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        # If the list has less then k items then push
        if(len(self.num) < self.k):
            heapq.heappush(self.num, val)
        # else push and pop the smallest item
        else:
            heapq.heappushpop(self.num, val)
          
        # kth largest is located at the index = 0
        return self.num[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
