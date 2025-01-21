# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        def has_k_nodes(node, k):
            count = 0
            while node and count < k:
                node = node.next
                count += 1
            return count == k

        if not has_k_nodes(head, k):
            return head

        cur = head
        prev = None
        for i in range(k):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        head.next = self.reverseKGroup(cur, k)

        return prev
