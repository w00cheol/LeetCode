class Solution:
    def mergeKLists(self, lists):
        head = ListNode(2e9)
        answer = head
        
        k = len(lists)
        dic = {}
        cnt = 0
        
        for i in range(k):
            temp = lists[i]
            if temp:
                dic[i] = temp.val
            while temp:
                cnt += 1
                temp = temp.next
                
        if cnt == 0:
            return None
        
        while cnt > 0:
            target = min(dic.items(), key=lambda x: x[1])
            answer.val = target[1]
            
            answer.next = ListNode(2e9) if cnt > 1 else None
            answer = answer.next
            
            lists[target[0]] = lists[target[0]].next
            
            if lists[target[0]] is not None:
                dic[target[0]] = lists[target[0]].val
            else:
                del dic[target[0]]
            
            cnt -= 1
                
        return head