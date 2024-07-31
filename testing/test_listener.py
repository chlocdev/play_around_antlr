"""
python test_listener.py path/to/file
"""
import sys
import time
import pandas as pd
from antlr4 import *
from ExprLexer import ExprLexer
from MyExprParser import ExprParser
from MyExprListener import ExprListener

# Init
print_out = True # print debug option
file_path = sys.argv[1]
tmp_path = '...' # custom
encoding = 'utf-8'

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

    # Walk around tree
    listener = ExprListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    # Export Lists
    export_list(listener.footprints, './footprints.txt')
    export_list(listener.sequences, './sequences.txt')

    # Export the parsed JCL data to a CSV file
    df_summary = pd.DataFrame(listener.summary)
    df_summary_transposed = df_summary.transpose()
    print(df_summary_transposed)
    df_summary_transposed.to_csv('./listener_report.csv', index=True)
    print(f"Exported ./listener_report.csv")