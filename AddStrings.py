class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        cv=itertools.izip_longest(num1[::-1],num2[::-1],fillvalue = '0')
        result, carry = [], 0
        for val in cv:
            n1 = ord(val[0]) - ord('0')
            n2 = ord(val[1]) - ord('0')
            sumOfNos = n1 + n2 + carry
            carry=sumOfNos // 10
            rem = sumOfNos % 10
            result.append(str(rem))
        if carry != 0:
            result.append(str(carry))
            
        if len(result[::-1]) > 0:
            res = ''.join(result[::-1])
            return res
        else:
            return str(0)
        
            
        