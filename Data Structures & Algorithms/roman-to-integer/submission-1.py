class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0;
        next = 0
        
        roman_numerals = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        if len(s) == 1:
            return roman_numerals[s]
        
        for i in range(len(s)-1):
            char = s[i]
            nextChar = s[i+1]
            next = roman_numerals[nextChar]

            if(roman_numerals[char] < next):
                total -= roman_numerals[char]
            else:
                total += roman_numerals[char]
            
        return (total + next)