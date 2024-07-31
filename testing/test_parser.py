"""
python test_parser.py path/to/file
"""
import sys
import time
from antlr4 import *
from ExprLexer import ExprLexer
from MyExprParser import ExprParser

# Init
print_out = True # print debug option
file_path = sys.argv[1]
tmp_path = '...' # custom
encoding = 'utf-8' # 'shift-jis' or 'utf-8'

# Blocks of code
def export_list(footprints: list,file_path: str):
    """
    Function export list of footprints into text file
    Args:
        footprint (list): list of node name (only count in enter function)
        file_path (str): path of text file
    Returns:
        None
    """
    with open(file_path,'w') as f:
        for footprint in footprints:
            f.write(f"{footprint}\n")
    
    print(f"Exported {file_path}")

if __name__ == "__main__":

    with open(file_path,'rt',encoding=encoding) as f:
        st = f.read()

    with open(tmp_path,'wt',encoding=encoding) as f:
        f.write('\r\n'+st) # Move the cursor to begining of the file at the next line

    # Create instances
    input = FileStream(tmp_path, encoding=encoding) # Stream content of file and tokenize 
    lexer = ExprLexer(input) # Instance of Lexer
    stream = CommonTokenStream(lexer) # Instance of Stream
    stream.fill()
    parser = ExprParser(stream) # # Instance Parse
    parser.buildParseTrees =  True

    # Build tree
    start_time_build_tree = time.time()
    tree = parser.program()
    end_time_build_tree = time.time() - start_time_build_tree

    if print_out:
        print(f"Total time for generate tree {file_path}: {end_time_build_tree:.2f} seconds")

    print(parser.summary)

