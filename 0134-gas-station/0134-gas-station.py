class Solution:
    def canCompleteCircuit(self, gas, cost):
        answer, require, money = 0, 0, 0
        
        for i in range(len(gas)):
            money += gas[i] - cost[i]
            
            if money < 0:
                answer = i + 1
                require += money
                money = 0
                
        if money + require >= 0:
            return answer
        else:
            return -1