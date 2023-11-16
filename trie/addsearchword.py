class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False 

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()

            curr = curr.children[c]
        curr.end = True

    def search(self, word:str) -> bool:
        def dfs(j, root):
            curr = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    # condition unmet
                    return False
                
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]

            return curr.end
        
        return dfs(0, self.root)