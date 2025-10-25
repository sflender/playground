
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_leaf = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_leaf = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_leaf

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    def complete(self, prefix):
        # bfs search for all words with given prefix
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        words = []
        queue = [(node, prefix)]
        while queue:
            current_node, current_prefix = queue.pop(0)
            if current_node.is_leaf:
                words.append(current_prefix)
            for char, child_node in current_node.children.items():
                queue.append((child_node, current_prefix + char))
        return words
    
if __name__ == "__main__":
    trie = Trie()
    words = ["apple", "app", "apricot", "banana", "band", "bandana"]
    for word in words:
        trie.insert(word)

    print(trie.search("apple"))  # True
    print(trie.search("app"))    # True
    print(trie.search("appl"))   # False
    print(trie.starts_with("ban"))  # True
    print(trie.starts_with("bat"))  # False
    print(trie.complete("ap"))  # ['apple', 'app', 'apricot']
    print(trie.complete("ban"))  # ['banana', 'band', 'bandana']