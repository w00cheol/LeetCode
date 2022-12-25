class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        runner = head
        
        while runner is not None:
            while runner.next and runner.val == runner.next.val:
                runner.next = runner.next.next
            
            runner = runner.next
        
        return head