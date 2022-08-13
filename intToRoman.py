class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # 2 lists could have been a dictionary?
        r = [ "I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
        l = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        # output variable
        roman = ""
        n = len(l)  
        while num != 0:
            # if the number is greater OR equal than... the roman numeral is added 
            if num >= l[n-1]:
                roman += r[n-1]
                num -= l[n-1]
            else: 
                n -= 1
        
        return roman
