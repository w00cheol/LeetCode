class Trie:
    answer = []
    def __init__(self):
        self.answer = set()
        
    def insert(self, word: str) -> None:
        self.answer.add(word)
    def search(self, word: str) -> bool:
        return word in self.answer
    def startsWith(self, prefix: str) -> bool:
        return any(map(lambda x: x.startswith(prefix), self.answer))