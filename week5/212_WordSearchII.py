class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        m, n = len(board), len(board[0])
        DIR = [0, 1, 0, -1, 0]
        trieNode = TrieNode()
        res = []
        for word in words:
            trieNode.insert(word)

        def dfs(r, c, cur):
            if r < 0 or r == m or c < 0 or c == n or board[r][c] not in cur.child: return
            orgChar = board[r][c]
            cur = cur.child[orgChar]
            board[r][c] = '#' 
            if cur.word != None:
                res.append(cur.word)
                cur.word = None
            for i in range(4): dfs(r + DIR[i], c + DIR[i + 1], cur)
            board[r][c] = orgChar

        for r in range(m):
            for c in range(n):
                dfs(r, c, trieNode)
        return res

class TrieNode:
    def __init__(self):
        self.child = defaultdict(TrieNode)
        self.word = None

    def insert(self, word):
        cur = self
        for c in word:
            cur = cur.child[c]
        cur.word = word
