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

