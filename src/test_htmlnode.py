import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTLMNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(
            "p",
            "This is a HTML node"
        )
        self.assertEqual(
            node.tag, 
            "p")
        self.assertEqual(
            node.value,
            "This is a HTML node"
        )
        self.assertEqual(
            node.children,
            None
        )
        self.assertEqual(
            node.props,
            None
        )
    
    def test_repr(self):
        node = HTMLNode(
            "p",
            "This node has the primary class attribute",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(), 
            "HTMLNode(p, This node has the primary class attribute, children: None, {'class': 'primary'})",
            )

    def test_props_to_html(self):
        node = HTMLNode(
            "a",
            "This links to google.com",
            None,
            {
                "href": "https://www.google.com", 
                "target": "_blank",
            }
        )
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com" target="_blank"',
        )

    def test_leaf_node_eq(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "This is a paragraph of text.")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)
    
    def test_to_html_leaf(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
    
    def test_to_html_no_tag(self):
        node = LeafNode(None, "Text dump here")
        self.assertEqual(node.to_html(), "Text dump here")

if __name__ == "__main__":
    unittest.main()