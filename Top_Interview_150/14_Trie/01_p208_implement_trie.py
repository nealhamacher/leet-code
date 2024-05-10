class Node(object):
    def __init__(self):
        self.children = {}
        self.isLastLetter = False

class Trie(object):

    def __init__(self):
        self.root = Node()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        current = self.root
        for letter in word:
            if letter not in current.children.keys():
                current.children[letter] = Node()
            current = current.children[letter]
        current.isLastLetter = True
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        current = self.root
        for letter in word:
            if letter not in current.children.keys():
                return False
            current = current.children[letter]
        if current.isLastLetter:
            return True
        else:
            return False
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for letter in prefix:
            if letter not in current.children.keys():
                return False
            current = current.children[letter]
        return True


################################################################################

if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))
    trie.insert("app")
    print(trie.startsWith("app"))
    print(trie.search("appleb"))