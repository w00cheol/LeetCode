class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer = head
        cnt = 0
        
        while head:
            if cnt % 2 == 0:
                if head.next:
                    head.val, head.next.val = head.next.val, head.val
                    
            cnt += 1
            head = head.next
            
        return answer