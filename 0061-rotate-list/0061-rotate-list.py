class Solution:
    def rotateRight(self, head, k: int):
        if head is None or head.next is None:
            return head
        new_head = head
        runner = head
        
        node_nums = 1
        for _ in range(k):
            if runner.next is None:
                runner = head
                
                for _ in range(k % node_nums):
                    runner = runner.next
                    
                break
            else:
                runner = runner.next
                node_nums += 1
            
            
        while runner.next is not None:
            runner = runner.next
            new_head = new_head.next
        
        runner.next = head
        
        temp = new_head
        new_head = new_head.next
        temp.next = None
        
        return new_head