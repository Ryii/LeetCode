ones = ["", " One", " Two", " Three", " Four", " Five", " Six", " Seven", " Eight", " Nine", " Ten", " Eleven", " Twelve", " Thirteen", " Fourteen", " Fifteen", " Sixteen", " Seventeen", " Eighteen", " Nineteen"]
tens = ["", " Ten", " Twenty", " Thirty", " Forty", " Fifty", " Sixty", " Seventy", " Eighty", " Ninety"]
hundreds = ["", " Thousand", " Million", " Billion"]

class Solution:
    def helper(self, num: int) -> str:
        if num < 20:
            return ones[num]
        if num < 100:
            return tens[num // 10] + self.helper(num % 10)
        if num < 1000:
            return ones[num // 100] + " Hundred" + self.helper(num - (num // 100) * 100)
        for i in range(3, -1, -1):
            power = pow(10, 3 * i)
            if num >= pow(10, 3 * i):
                remainder = num - (num // power) * power
                return self.helper(num // power) + hundreds[i] + self.helper(remainder)
        return "failed"
    
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        return self.helper(num)