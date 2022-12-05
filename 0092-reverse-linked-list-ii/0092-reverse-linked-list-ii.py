class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        fake = ListNode(0, head)
        runner = fake
        
        for _ in range(left - 1):
            runner = runner.next
            
        last_head = runner
        runner = runner.next
        
        tail = runner
        prev = runner
        curr = runner.next
        
        for _ in range(right - left):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        last_head.next = prev 
        tail.next = curr
            
        return fake.next