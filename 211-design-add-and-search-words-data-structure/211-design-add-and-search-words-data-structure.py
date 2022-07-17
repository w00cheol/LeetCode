class WordDictionary:
    def __init__(self):
        self.dic = {}

    def addWord(self, word: str) -> None:
        d = self.dic
        for w in word:
            if w not in d: d[w] = {}
            d = d[w]
        d['end'] = True

    def dfs(self, d, word):
        if not word:
            if 'end' in d: return True
            return False
        for key in d.keys():
            if key != 'end' and word[0] == '.' or word[0] == key:
                if self.dfs(d[key], word[1:]): return True
        return False
    def search(self, word: str) -> bool:
        return self.dfs(self.dic, word)