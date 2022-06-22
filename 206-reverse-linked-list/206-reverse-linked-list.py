class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return head
        answer = ListNode(head.val)
        head = head.next
        while head is not None:
            answer = ListNode(head.val, answer)
            head = head.next
        return answer