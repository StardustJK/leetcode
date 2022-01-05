#
# @lc app=leetcode.cn id=208 lang=python
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
class Trie(object):

    def __init__(self):
        self.children=[None]*26
        self.isEnd=False


    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node=self
        for ch in word:
            index=ord(ch)-ord('a')
            if node.children[index]:
                node=node.children[index]
            else:
                node.children[index]=Trie()
                node=node.children[index]
        node.isEnd=True
        return None


    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """

        node=self
        for ch in word:
            index=ord(ch)-ord('a')
            if node.children[index]:
                node=node.children[index]
            else:
                return False

        return node.isEnd

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node=self
        for ch in prefix:
            index=ord(ch)-ord('a')
            if node.children[index]:
                node=node.children[index]
            else:
                return False
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

