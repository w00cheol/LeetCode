class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]):
        answer_head = answer_runner = ListNode(None)
        num = -2e9
        
        while head:
            # pass duplicated nodes quickly
            while head and num == head.val:
                head = head.next
               
            if head:
                # reset num
                num = head.val
                
                # decide whether to add this new node or not
                # by predicting if it will be duplicated
                if head.next is None or num != head.next.val:
                    answer_runner.next = ListNode(num)
                    answer_runner = answer_runner.next
                    head = head.next
            
        return answer_head.next