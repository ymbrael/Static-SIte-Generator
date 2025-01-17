import re
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
    
        split_nodes = []
        splits = old_node.text.split(delimiter)
        if len(splits) % 2 == 0:
            raise ValueError("Invalid Markdown Syntax, no closing delimiter")
        for i in range(len(splits)):
            if splits[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(splits[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(splits[i], text_type))
        
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\(]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def split_nodes_image(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        old_text = old_node.text
        images = extract_markdown_images(old_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue

        for image in images:
            splits = old_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(splits) != 2:
                raise ValueError("Invalid Markdown Syntax, image section not closed")
            if splits[0] != "":
                new_nodes.append(TextNode(splits[0], TextType.TEXT))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            old_text = splits[1]

        if old_text != "":
            new_nodes.append(TextNode(old_text, TextType.TEXT))
    
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        old_text = old_node.text
        links = extract_markdown_links(old_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            splits = old_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(splits) != 2:
                raise ValueError("Invalid Markdown Syntax, link section not closed")
            if splits[0] != "":
                new_nodes.append(TextNode(splits[0], TextType.TEXT))
            new_nodes.append(TextNode(
                link[0],
                TextType.LINK,
                link[1],
                )
            )
            old_text = splits[1]
        
        if old_text != "":
            new_nodes.append(TextNode(old_text, TextType.TEXT))
    
    return new_nodes


def text_to_text_nodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    new_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        new_blocks.append(block)
    return new_blocks

    