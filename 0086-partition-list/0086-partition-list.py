class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left, right = ListNode(None), ListNode(None)
        left_runner, right_runner, runner = left, right, head
        
        while runner:
            if runner.val < x:
                left_runner.next = ListNode(runner.val)
                left_runner = left_runner.next
            else:
                right_runner.next = ListNode(runner.val)
                right_runner = right_runner.next
                
            runner = runner.next
        
        left_runner.next = right.next
        
        return left.next