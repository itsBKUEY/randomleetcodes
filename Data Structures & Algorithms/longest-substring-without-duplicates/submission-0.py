class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hashset = set()
        fast = 0
        slow = 0
        largest = 0

        while( fast < len(s)):
            while( s[fast] in hashset):
                hashset.remove(s[slow])
                slow += 1
            hashset.add(s[fast])
            fast +=1
            largest = max(largest, fast-slow)

        return largest

            
        