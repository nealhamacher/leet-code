class Node(object):
    def __init__(self):
        self.children = {}
        self.isLastLetter = False

class WordDictionary(object):

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word):
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
        return self.search_recursive(word, self.root)
        
    def search_recursive(self, word, node):
        if word == '.' and len(node.children) > 0:
            return True
        if word == "":
            if node.isLastLetter:
                return True
            else:
                return False
        

        current = word[0]
        if current == ".":
            # Go through all children
            for child in node.children.values():
                # If any return true, a match is found
                if (self.search_recursive(word[1:], child)):
                    return True
            return False

        else:
            if current not in node.children.keys():
                return False
            else:
                return self.search_recursive(word[1:], node.children[current])

            
################################################################################        

if __name__ == "__main__":
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")
    print(wd.search("pad"))
    print(wd.search("bad"))
    print(wd.search(".ad"))
    print(wd.search("b.."))
    print(wd.search("b..."))
    print(wd.search("..g"))
