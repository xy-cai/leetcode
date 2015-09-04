# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        if not head.next:
            return True
            
        # Find the middle of list, and reverse the first half
        p1 = head
        p2 = head
        pre = None
        flag = 1
        while p2:
            if not p2.next:
                flag = 2
                break
            
            p2 = p2.next.next
            
            nx = p1.next
            p1.next = pre
            pre = p1
            p1 = nx
            
        
        if flag == 1:
            p2 = p1
        else:
            p2 = p1.next
        p1 = pre
        
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        
        return True