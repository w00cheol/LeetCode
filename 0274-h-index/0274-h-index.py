class Solution:
    def hIndex(self, citations):
        answer = 0
        citations.sort(reverse = True)
        
        for citation in citations:
            answer += 1
            
            if answer > citation:
                return answer - 1
        
        return answer