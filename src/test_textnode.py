import unittest

from textnode import TextNode, TextType, text_node_to_html_node


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


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        t_node = TextNode("This node contains plain text", TextType.TEXT)
        h_node = text_node_to_html_node(t_node)
        self.assertEqual(h_node.tag, None)
        self.assertEqual(h_node.value, "This node contains plain text")
        self.assertEqual(h_node.props, None)

    def test_link(self):
        t_node = TextNode("This node contains a link", TextType.LINK, "https://www.boot.dev")
        h_node = text_node_to_html_node(t_node)
        self.assertEqual(h_node.tag, "a")
        self.assertEqual(h_node.value, "This node contains a link")
        self.assertEqual(h_node.props, {"href": "https://www.boot.dev"})

    def test_image(self):
        t_node = TextNode("Wow, very test image", TextType.IMAGE, "https://github.com/ymbrael")
        h_node = text_node_to_html_node(t_node)
        self.assertEqual(h_node.tag, "img")
        self.assertEqual(h_node.value, "")
        self.assertEqual(h_node.props,
            {"src": "https://github.com/ymbrael", "alt": "Wow, very test image"}
            )


if __name__ == "__main__":
    unittest.main()