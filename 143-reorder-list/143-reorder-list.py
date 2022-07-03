class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        prev, slow, fast = None, head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        left, right = head, prev
        while right and right.next:
            copy_left = left.next
            left.next = right
            copy_right = right.next
            right.next = copy_left
            left, right = copy_left, copy_right