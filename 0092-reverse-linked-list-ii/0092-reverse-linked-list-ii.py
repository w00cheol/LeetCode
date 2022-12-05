class Solution:
    def reverseBetween(self, head, left, right):
        # insert dummy node O(1)
        fake_head = ListNode(None)
        fake_head.next = head
        
        curr = fake_head
        
        # skip to (left - 1) O(N)
        for _ in range(left - 1):
            curr = curr.next
            
        last_head = curr # index = left - 1
        
        curr = curr.next # index += 1
        last_body = curr # index = left
        
        # prev, curr index = left, left + 1
        prev = curr
        curr = curr.next
        
        # reverse two nodes O(n)
        # shift each variable one index to right side
        for _ in range(right - left):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        # combine three parts into one
        last_head.next = prev 
        last_body.next = curr
            
        # return real head
        return fake_head.next