import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a link node", TextType.LINK, "www.google.com")
        self.assertNotEqual(node, node2)

    def test_type(self):
        node = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node.text_type, TextType.TEXT)

    def test_url(self):
        node = TextNode("This is a link", TextType.LINK, "archlinux.org")
        self.assertNotEqual(node.url, None)


if __name__ == "__main__":
    unittest.main()
