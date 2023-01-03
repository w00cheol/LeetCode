class Solution:
    def hIndex(self, citations):
        answer = 0
        citations.sort(reverse = True)
        
        for citation in citations:
            if answer + 1 > citation:
                break
                
            answer += 1
        
        return answer