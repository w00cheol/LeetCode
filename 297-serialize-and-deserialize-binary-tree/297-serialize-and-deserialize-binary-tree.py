class Codec:
    def dfs(self, data):
        if data[:2] == 'N+': return data[2:], None
        index = data.find('+')
        root = TreeNode(int(data[:index]))
        data = data[index+1:]
        data, root.left = self.dfs(data)
        data, root.right = self.dfs(data)
        return data, root
    
    def serialize(self, root, answer_str = ''):
        if not root:
            answer_str += 'N+'
        else:
            answer_str += str(root.val)
            answer_str += '+'
            answer_str = self.serialize(root.left, answer_str)
            answer_str = self.serialize(root.right, answer_str)
        return answer_str

    def deserialize(self, data):
        garbage, answer_node = self.dfs(data)
        return answer_node