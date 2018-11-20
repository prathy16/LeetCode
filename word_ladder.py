'''
Problem: https://leetcode.com/problems/word-ladder/
'''

from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        def dict_words(wordList):
            d = {}
            
            for word in wordList:
                for i in range(len(word)):
                    s    = word[:i] + "_" + word[i+1:]
                    d[s] = d.get(s, []) + [word]
                    
            return d
        
        def steps_queue(beginWord, endWord, d):
            queue, visited = deque([(beginWord, 1)]), set()
            
            while(queue):
                word, steps = queue.popleft()
                if word == endWord: 
                    return steps
                if word not in visited:
                    visited.add(word)
                    
                    for i in range(len(word)): 
                        s = word[:i] + "_" + word[i+1:]
                        for each_word in d.get(s, []):
                            if each_word not in visited:
                                queue.append((each_word, steps+1))
                                if(each_word == endWord): 
                                    return (steps + 1)
            return 0
                    
        
        d = dict_words(wordList)
        return steps_queue(beginWord, endWord, d)
        
