'''
Problem: https://leetcode.com/problems/repeated-dna-sequences/
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]
'''

class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        start, end           = 0, 10
        hash_table, ret_list = {}, set()
        
        while(start < end and end <= len(s)):
            if s[start:end] not in hash_table:
                hash_table[s[start:end]] = 1
            else:
                ret_list.add(s[start:end])
    
            start, end = start+1, end+1
        
        return list(ret_list)
