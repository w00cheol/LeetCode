class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        remove_index, interval_remove_index = head, head
        for _ in range(n):
            interval_remove_index = interval_remove_index.next
        if interval_remove_index is None:
            return head.next
        while interval_remove_index.next:
            remove_index, interval_remove_index = remove_index.next, interval_remove_index.next
        remove_index.next = remove_index.next.next
        return head