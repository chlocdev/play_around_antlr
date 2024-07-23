'''
python langs/Hello/visualize_tree.py langs/Hello/examples/hello.txt
'''
import os
import sys
from antlr4 import *
from HelloLexer import HelloLexer as Lexer
from HelloParser import HelloParser as Parser
from antlr4.tree.Trees import Trees
from graphviz import Digraph

# Init
print("Import Successful!")

def get_node_name(node) ->str:
    """
    Function Extract Node Type
    
    Args:
        node: Node
    Returns:
        node_name: Name of Node
    """
    # init
    node_name = "Unknown"
    raw_type_string = str(type(node))

    if "TerminalNode" in raw_type_string:
        node_name = str(node)
        return node_name.strip()

    # find the start-end positions
    start_index = raw_type_string.find("'")  # Find the first occurrence of '
    end_index = raw_type_string.rfind("'")   # Find the last occurrence of '

    if start_index != -1 and end_index != -1:
        node_name = raw_type_string[start_index + 1:end_index]
        node_name = node_name.split('.')[-1]
        #node_name = node_name.replace("Context","")
    
    return node_name

def traverse_tree(dot, tree):
    # If current tree is not a leaf-node
    if tree.getChildCount() > 0:
        # Get parent string
        parent_str = get_node_name(tree)
        for child in tree.children:
            # Get child string
            child_str = get_node_name(child)
            # Give a edge from parent - child
            dot.edge(parent_str, child_str)
            # Continue traverse to recursively
            traverse_tree(dot, child)

def visualize_parse_tree(input_string)->None:

    input_stream = InputStream(input_string)
    lexer = Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Parser(stream)
    tree = parser.r() # custom here

    # Convert parse tree to string representation
    tree_str = Trees.toStringTree(tree, None, parser)

    # Create a graphviz Digraph
    dot = Digraph()
    traverse_tree(dot, tree)

    # Render and display the parse tree
    dot.render('parse_tree', format='png', view=True)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        
        input_string_path = sys.argv[1]
        
        # Read input string content
        with open(input_string_path,'r') as f:
            input_string = f.read()

        input_string = input_string.strip()
        
        print(f"{input_string_path}\n{input_string}")
 
        visualize_parse_tree(input_string)
    else:
        print("Please provide an input string path.")