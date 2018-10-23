'''
Problem: https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp1, temp2 = l1, l2
        temp3, l3 = None, None
        num1, num2 = [], []
        rev_num1, rev_num2 = 0, 0
        
        # Traverse through the LL to get list of digits
        while(temp1):
            num1.append(temp1.val)
            temp1 = temp1.next
        while(temp2):
            num2.append(temp2.val)
            temp2 = temp2.next
            
        # convert the list of digits into integer numbers
        rev_num1, rev_num2 = int(''.join(str(i) for i in num1[::-1])), int(''.join(str(i) for i in num2[::-1])) 
        
        # Add both the numbers
        num = rev_num1+ rev_num2
        str_num = str(num)
        list_digits = [int(x) for x in str_num]
        
        # traverse through each digit of the summation of numbers and insert a new node into LL
        for digit in list_digits[::-1]:
            if(l3 == None):
                l3 = ListNode(int(digit))
                temp3 = l3
            else:
                temp_temp3 = ListNode(int(digit))
                temp3.next = temp_temp3
                temp3 = temp_temp3
        return l3
                
