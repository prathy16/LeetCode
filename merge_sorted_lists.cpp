# https://leetcode.com/problems/merge-two-sorted-lists/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        
        ListNode newList(0);
        ListNode* newheader = &newList;
        
        while(l1 && l2)
        {
            if(l1->val < l2->val)
            {
                newheader->next = l1;
                l1 = l1->next;
            }
            else
            {
                newheader->next = l2;
                l2 = l2->next;
            }
            
            newheader = newheader->next;
        }
        
        newheader->next = l1 ? l1 : l2;
        
        return newList.next;
    }
};
