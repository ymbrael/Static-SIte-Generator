import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_3_nodes(self):
        node = TextNode("All these text nodes are the same", TextType.ITALIC)
        node2 = TextNode("All these text nodes are the same", TextType.ITALIC)
        node3 = TextNode("All these text nodes are the same", TextType.ITALIC)
        self.assertEqual(node, node2, node3)
    
    def test_missing_url(self):
        node = TextNode("This text node links to Ymbrael's github", TextType.LINK, "https://github.com/ymbrael")
        node2 = TextNode("This text node links to Ymbrael's github", TextType.LINK, None)
        self.assertNotEqual(node, node2)

    def test_noteq(self):
        node = TextNode("These text nodes have different types", TextType.TEXT)
        node2 = TextNode("These text nodes have different types", TextType.CODE)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()