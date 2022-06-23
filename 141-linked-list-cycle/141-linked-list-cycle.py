# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        step1 = step2 = head
        while step1 and step2 and step2.next:
            step1 = step1.next
            step2 = step2.next.next
            if step1 == step2:
                return True
        return False