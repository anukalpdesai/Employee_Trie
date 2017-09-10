import unittest
from ..trie import Trie


class TestEmployeeTrie(unittest.TestCase):

    def test_trie(self):
        trie = Trie()
        self.assertIsNone(trie.root.val, None)

    def test_trie_insert_single_word(self):
        trie = Trie()
        word = 'hellO'
        trie.insert(word)
        root = trie.root
        self.assertEqual(root.child['h'].val, 'h')
        root = root.child['h']
        self.assertEqual(root.child['e'].val, 'e')
        root = root.child['e']
        self.assertEqual(root.child['l'].val, 'l')
        root = root.child['l']
        self.assertEqual(root.child['l'].val, 'l')
        root = root.child['l']
        self.assertEqual(root.child['o'].val, 'o')
        root = root.child['o']
        self.assertEqual(root.is_word, True)

    def test_trie_insert_two_words(self):
        trie = Trie()
        trie.insert('hello')
        trie.insert('Hel')

        root = trie.root

        self.assertEqual(root.child['h'].val, 'h')
        root = root.child['h']
        self.assertEqual(root.child['e'].val, 'e')
        root = root.child['e']
        self.assertEqual(root.child['l'].val, 'l')

        root = root.child['l']
        self.assertTrue(root.is_word)

        self.assertEqual(root.child['l'].val, 'l')
        root = root.child['l']
        self.assertEqual(root.child['o'].val, 'o')

        root = root.child['o']
        self.assertTrue(root.is_word)

    def test_trie_search_two_words(self):
        trie = Trie()

        trie.insert('Hello')
        trie.insert('Hell')

        self.assertTrue(trie.search('hello'))
        self.assertTrue(trie.search('hell'))

        self.assertFalse(trie.search('hellp'))

if __name__ == "__main__":
    unittest.main()