# GFG question
class Solution:
	def binaryToDecimal(self, b):
		# Code here
		decimalValue = int(b,2)
# 		base = 1
# 		while(b != 0):
# 		    remainder = b % 10
# 		    b /= 10
# 		    decimalValue = remainder * base
# 		    base *= 2
		return decimalValue
