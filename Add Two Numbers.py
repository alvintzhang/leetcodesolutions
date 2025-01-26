# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        x = []
        y = []
        while l1:
            x.append(l1.val)
            l1 = l1.next
        while l2:
            y.append(l2.val)
            l2 = l2.next

        cur1 = 0
        cur2 = 0
        i = len(x)
        j = len(y)
        while i > 0:
            cur1 += x[i - 1] * (10 ** (i - 1))
            i -= 1
        while j > 0:
            cur2 += y[j - 1] * (10 ** (j - 1))
            j -= 1

        cur3 = cur1 + cur2
        digits = []
        while cur3 > 0:
            digits.insert(0, cur3 % 10)
            cur3 //= 10
        
        if not digits: #Case 2
            digits.append(0) 

        digits.reverse()

        dummy = ListNode()
        current = dummy
        for digit in digits:
            current.next = ListNode(digit)
            current = current.next

        return dummy.next
