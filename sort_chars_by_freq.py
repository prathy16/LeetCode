'''
Problem: [https://leetcode.com/problems/sort-characters-by-frequency](https://leetcode.com/problems/sort-characters-by-frequency)
Given a string, sort it in decreasing order based on the frequency of characters.
'''

class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        return "".join(character*count for character, count in collections.Counter(s).most_common())
