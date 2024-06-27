class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

    class Trie:

        def __init__(self):
            self.root = TrieNode()

        def insert(self, word: str) -> None:
            node = self.root
            for l in word:
                if l not in node.children:
                    node.children[l] = TrieNode()
                node = node.children[l]
            node.is_word = True

        def search(self, word: str) -> bool:
            node = self.root
            for l in word:
                if l not in node.children:
                    return False
                node = node.children[l]
            return node.is_word

        def startsWith(self, prefix: str) -> bool:
            node = self.root
            for l in prefix:
                if l not in node.children:
                    return False
                node = node.children[l]
            return True


# Your Trie object will be instantiated and called as such:
obj = TrieNode().Trie()
obj.insert("apple")
param_2 = obj.search("apple")
param_3 = obj.startsWith("app")
print(param_2, param_3)


class Trie2:
    """
    simply use dictionary, add "*" to indicate it is the word
    """
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:

        cur = self.root

        for letter in word:
            if letter not in cur:
                cur[letter] = {}
            cur = cur[letter]

        cur['*'] = ''

    def search(self, word: str) -> bool:

        cur = self.root
        for letter in word:
            if letter not in cur:
                return False
            cur = cur[letter]

        return '*' in cur

    def startsWith(self, prefix: str) -> bool:

        cur = self.root
        for letter in prefix:
            if letter not in cur:
                return False
            cur = cur[letter]

        return True