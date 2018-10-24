'''
Problem: https://leetcode.com/problems/fruit-into-baskets/
In a row of trees, the i-th tree produces fruit with type tree[i].

You start at any tree of your choice, then repeatedly perform the following steps:

Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?
'''

class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        fruit_count, start = 0, 0
        baskets = collections.Counter()
        
        for ind, fruit_type in enumerate(tree):
            baskets[fruit_type] += 1
            while(len(baskets) == 3):
                baskets[tree[start]] -= 1
                if(baskets[tree[start]] == 0):
                    del baskets[tree[start]]
                start += 1
            fruit_count = max(fruit_count, ind-start+1)
            
        return fruit_count
