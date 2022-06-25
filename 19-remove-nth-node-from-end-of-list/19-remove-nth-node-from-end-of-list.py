class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        here, interval_here = head, head
        for _ in range(n):
            interval_here = interval_here.next
        if not interval_here:
            return head.next
        while interval_here.next:
            here, interval_here = here.next, interval_here.next
        here.next = here.next.next
        return head