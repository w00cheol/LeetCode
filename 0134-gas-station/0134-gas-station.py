class Solution:
    def canCompleteCircuit(self, gas, cost):
        diff = [gas[i] - cost[i] for i in range(len(gas))]
        
        answer = 0
        require, money = 0, 0
        
        for i in range(len(diff)):
            money += diff[i]
            
            if money < 0:
                answer = i + 1
                require += money
                money = 0
                
        if money + require >= 0:
            return answer
        else:
            return -1