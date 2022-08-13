class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # dictionary
        dic = {"I": 1, 
               "V": 5, 
               "X": 10, 
               "L": 50, 
               "C": 100, 
               "D": 500, 
               "M": 1000}
        
        # number out put what roman number represents 
        num = 0
        
        #going through each character in roman number
        for i in range(len(s)):
            # if last character in roman number OR the value is greater than the next number 
            if i==len(s)-1 or dic[s[i]] >= dic[s[i+1]]:
                num += dic[s[i]] 
            else:
                # when number is less then the next number it will be subtracted 
                num -= dic[s[i]]
        # return roman as an int
        return num
