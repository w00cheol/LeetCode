class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head
        
        new_head, runner = head, head
        
        node_nums = 1
        for _ in range(k):
            if runner.next:
                runner = runner.next
                node_nums += 1
            else:
                runner = head
                
                for _ in range(k % node_nums):
                    runner = runner.next
                    
                break
            
        while runner.next:
            runner = runner.next
            new_head = new_head.next
        
        runner.next = head
        
        temp = new_head
        new_head = new_head.next
        temp.next = None
        
        return new_head