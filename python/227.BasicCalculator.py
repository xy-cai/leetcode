class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        def calc (a, b, op):
            return {'+':lambda x,y:x+y, '-':lambda x,y:x-y, '*':lambda x,y:x*y, '/':lambda x,y:x/y}[op](a,b)
            
        nums = []
        ops = []
        num = -1
        for ele in s:
            if ele == " ":
                if num != -1:
                    nums.append(num)
                    num = -1
                continue
            elif ele in "+-*/":
                if num != -1:
                    nums.append(num)
                    num = -1
                ops.append(ele)
            else:
                if num==-1:
                    num = 0
                num *= 10
                num += int(ele)
        if num != -1:
            nums.append(num)
        # print nums
        # print ops
        # print len(nums), len(ops)

        if len(ops) == 0:
            return nums[0]

        stack_num = [0]*2
        stack_num[0] = nums[0]
        op = ""
        top = 0
        i = 0
        while i<len(ops):
            if ops[i] in '+-':
                if top>0:
                    stack_num[0] = calc(stack_num[0], stack_num[1], op)
                stack_num[1] = nums[i+1]
                op = ops[i]
                top = 1
            else:
                stack_num[top] = calc(stack_num[top], nums[i+1], ops[i])
            i += 1

        if top>0:
            stack_num[0] = calc(stack_num[0], stack_num[1], op)

        return stack_num[0]
