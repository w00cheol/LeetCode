class Trie:
    answer = []
    def __init__(self):
        self.answer = set()
    def insert(self, word):
        self.answer.add(word)
    def search(self, word):
        return word in self.answer
    def startsWith(self, prefix):
        return any(map(lambda x: x.startswith(prefix), self.answer))