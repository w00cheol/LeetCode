class Solution:
    def copyRandomList(self, head):
        dic = {}
        
        runner = head
        
        while runner:
            dic[runner] = Node(runner.val)
            runner = runner.next
            
        runner = head
        
        while runner:
            curr = dic.get(runner)
            curr.next = dic.get(runner.next)
            curr.random = dic.get(runner.random)
            runner = runner.next
            
        return dic.get(head)