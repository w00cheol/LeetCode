class Solution:
    def zigzagLevelOrder(self, root):
        
        def divide_conquer(root, depth):
            if root is None: return {}
            
            small_answer = {}
            small_answer[depth] = [root.val]
                
            l = divide_conquer(root.left, depth + 1)
            r = divide_conquer(root.right, depth + 1)
            
            conquered_level = depth + 1
            conquered_l = l.get(conquered_level, [])
            conquered_r = r.get(conquered_level, [])
            
            while conquered_l != [] or conquered_r != []:
                if conquered_level % 2 == 0:
                    small_answer[conquered_level] = conquered_r + conquered_l
                else:
                    small_answer[conquered_level] = conquered_l + conquered_r
                    
                conquered_level += 1
                conquered_l = l.get(conquered_level, [])
                conquered_r = r.get(conquered_level, [])
            
            return small_answer
        
        answer = divide_conquer(root, 1)
        return answer.values()