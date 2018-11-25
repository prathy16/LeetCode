'''
Problem: https://leetcode.com/problems/unique-word-abbreviation/
'''

class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.d = collections.defaultdict(set)
        
        for word in dictionary:
            temp = word
            if len(word) > 2:
                word = word[0] + str(len(word) -2) + word[-1]
                
            self.d[word].add(temp)
        
    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        temp = word
        
        if len(word) > 2:
            word = word[0] + str(len(word)-2) + word[-1]
            
        return len(self.d[word]) == 0 or (len(self.d[word]) == 1 and temp == list(self.d[word])[0])
                
        
# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
