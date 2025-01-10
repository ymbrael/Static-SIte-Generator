import unittest

from htmlnode import HTMLNode

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


if __name__ == "__main__":
    unittest.main()