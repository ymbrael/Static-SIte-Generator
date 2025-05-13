import unittest
from markdown_blocks import markdown_to_blocks


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """
**Bold paragraph goes here.**



*This paragraph has italic text*
as well as `code` text on another line.

* Down here we have a list
* with
* some
* things
"""
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(
            blocks,
            [
                "**Bold paragraph goes here.**",
                "*This paragraph has italic text*\nas well as `code` text on another line.",
                "* Down here we have a list\n* with\n* some\n* things"
            ]
        )

    #temp test copied from course, raplce later
    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

if __name__== "__main__":
    unittest.main()