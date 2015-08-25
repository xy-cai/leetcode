import re

class Solution(object):
	def diffWaysToCompute(self, input):
		"""
		:type input: str
		:rtype: List[int]
		"""
		def calc(a, b, op):
			return {'+':lambda x,y:x+y, '-':lambda x,y:x-y, '*':lambda x,y:x*y}[op](a,b)

		def dfs(ops, nums):
			#print len(ops)
			#print len(nums)
			if len(ops)==0:
				return [nums[0]]

			ret = []

			for index, ele in enumerate(ops):
				left = dfs(ops[0:index], nums[0:index+1])
				right = dfs(ops[index+1:], nums[index+1:])
				# if ops[index] == '+':
				# 	for l in left:
				# 		for r in right:
				# 			ret.append(l+r)
				# elif ops[index] == '-':
				# 	for l in left:
				# 		for r in right:
				# 			ret.append(l-r)
				# else:
				# 	for l in left:
				# 		for r in right:
				# 			ret.append(l*r)
				for l in left:
					for r in right:
						ret.append(calc(l,r,ops[index]))
			return ret

		input = re.split(r'(\D)', input)
		ops = []
		nums = []
		for ele in input:
			if ele == '+' or ele == '-' or ele == '*':
				ops.append(ele)
			else:
				nums.append(int(ele))

		return dfs(ops, nums)