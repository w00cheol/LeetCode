class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev, curr = None, slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        left, right = head, prev
        while right and right.next:
            copy_left = left.next
            left.next = right
            copy_right = right.next
            right.next = copy_left
            left, right = copy_left, copy_right