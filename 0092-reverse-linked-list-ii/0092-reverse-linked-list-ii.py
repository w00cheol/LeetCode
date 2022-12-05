class Solution:
    def reverseBetween(self, head, left, right):
        fake_head = ListNode(0, head)
        curr = fake_head
        
        for _ in range(left - 1):
            curr = curr.next
            
        last_head = curr # idx : left - 1
        
        curr = curr.next # idx += 1
        last_body = curr # idx : left
        
        # prev, curr = left, left + 1
        prev = curr
        curr = curr.next
        
        # reverse and slide window
        for _ in range(right - left):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        last_head.next = prev 
        last_body.next = curr
            
        return fake_head.next