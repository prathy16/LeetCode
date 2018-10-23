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
        ll = None
        num1, num2 = [], []
        rev_num1, rev_num2 = 0, 0
        
        # Traverse through the LL to get list of digits
        temp1 = l1
        while(temp1):
            num1.append(temp1.val)
            temp1 = temp1.next
        temp1 = l2
        while(temp1):
            num2.append(temp1.val)
            temp1 = temp1.next
            
        # convert the list of digits into integer numbers and sum them up
        str_num = str(int(''.join(str(i) for i in num1[::-1])) + int(''.join(str(i) for i in num2[::-1]))) 

        list_digits = [int(x) for x in str_num]
        
        # traverse through each digit of the summation of numbers and insert a new node into LL
        temp = ll
        for digit in list_digits[::-1]:
            if(ll == None):
                ll = ListNode(int(digit))
                temp = ll
            else:
                temp.next = ListNode(int(digit))
                temp = temp.next
        return ll
                
