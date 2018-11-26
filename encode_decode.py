'''
Problem: https://leetcode.com/problems/encode-and-decode-strings/
'''
class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        return ''.join("%d:" % len(s)+s for s in strs)

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        ret_strings = []
        
        i = 0
        while(i < len(s)):
            j = s.find(':', i)
            i = j + int(s[i:j]) + 1
            
            ret_strings.append(s[j+1:i])
            
        return ret_strings

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
