class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.end = True
        

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return cur.end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
obj.insert("ape")
obj.insert("banana")
obj.insert("cat")
param_2 = obj.search("apple")
param_3 = obj.startsWith("app")
print(param_2)
print(param_3)