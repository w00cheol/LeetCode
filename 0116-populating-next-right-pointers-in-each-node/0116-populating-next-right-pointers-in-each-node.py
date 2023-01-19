class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        runner = root
        
        while runner:
            next_level_first = runner.left
            
            while runner:
                if runner.left:
                    runner.left.next = runner.right
                
                if runner.right and runner.next:
                    runner.right.next = runner.next.left
                    
                runner = runner.next
            
            runner = next_level_first
            
        return root