import logging


logging.basicConfig(level=logging.INFO,
                    format="%(funcName)s:%(lineno)d:%(message)s")


class Trie:

    class TrieNode:

        __slots__ = 'val', 'is_word', 'child', 'user_data'

        def __init__(self, val, is_word=False, user_data=None):
            self.val = val
            self.is_word = is_word
            self.child = dict()
            self.user_data = user_data

    def __init__(self):
        self.root = Trie.TrieNode(None)

    def insert(self, word):
        root = self.root

        logging.debug('word = %s', word)

        for char in word:
            char = char.lower()
            if root.child.get(char, None) is None:
                root.child[char] = Trie.TrieNode(char)
            root = root.child[char]
        root.is_word = True

        logging.debug('char = %s', root.val)
        logging.debug('is_word = %s', root.is_word)

    def search(self, word):
        root = self.root

        logging.debug('word = %s', word)

        for char in word:
            char = char.lower()
            if root.child.get(char, None) is None:
                return False
            root = root.child[char]
        return root.is_word





