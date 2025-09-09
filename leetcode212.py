from typing import List, Dict

class TrieNode:
    _slots_ = ("children", "word")
    def _init_(self):
        self.children: Dict[str, TrieNode] = {}
        self.word: str | None = None  # guarda a palavra completa quando termina aqui

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        # 1) monta o trie
        for w in words:
            node = root
            for ch in w:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = w  # marca fim de palavra

        m, n = len(board), len(board[0])
        res = []

        def dfs(r: int, c: int, node: TrieNode):
            ch = board[r][c]
            if ch not in node.children:
                return
            nxt = node.children[ch]

            # achou uma palavra
            if nxt.word is not None:
                res.append(nxt.word)
                nxt.word = None  # evita duplicatas

            # marca visitado
            board[r][c] = '#'
            if r > 0 and board[r-1][c] != '#':
                dfs(r-1, c, nxt)
            if r+1 < m and board[r+1][c] != '#':
                dfs(r+1, c, nxt)
            if c > 0 and board[r][c-1] != '#':
                dfs(r, c-1, nxt)
            if c+1 < n and board[r][c+1] != '#':
                dfs(r, c+1, nxt)
            # restaura
            board[r][c] = ch

          
            if not nxt.children and nxt.word is None:
                del node.children[ch]

        # 2) inicia DFS de cada célula
        for i in range(m):
            for j in range(n):
                dfs(i, j, root)

        return res