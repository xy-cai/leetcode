# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        ret = l1
        cur = l1
        flag = 0
        while l1 and l2:
            tem = l1.val+l2.val+flag
            cur.val = tem%10
            flag = tem/10
            l1 = l1.next 
            l2 = l2.next
            if not (l1 or l2):
                if flag:
                    cur.next = ListNode(1)
                    flag = 0
            elif l2:
                cur.next = l2
            else:
                cur.next = l1
            cur = cur.next
        while flag:
            tem = cur.val+1
            cur.val = tem%10
            flag = tem/10
            if (not cur.next) and flag:
                cur.next = ListNode(1)
                flag = 0
            cur = cur.next
        return ret
            