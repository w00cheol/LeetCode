class Trie:
    answer = []
    def __init__(self):
        self.answer = set()
        
    def insert(self, word: str):
        self.answer.add(word)
    def search(self, word: str):
        return word in self.answer
    def startsWith(self, prefix: str):
        return any(map(lambda x: x.startswith(prefix), self.answer))