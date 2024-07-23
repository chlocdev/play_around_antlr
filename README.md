# play_around_antlr
Antlr Python

        def traverse_tree_and_revert(dot, tree):
            traversal_log = []
            
            def traverse_and_log(tree):
                # If current tree is not a leaf-node
                if tree.getChildCount() > 0:
                    # Get parent string
                    parent_str = get_node_name(tree)
                    for child in tree.children:
                        # Get child string
                        child_str = get_node_name(child)
                        # Log the edge from parent to child
                        traversal_log.append((parent_str, child_str))
                        # Continue traverse recursively
                        traverse_and_log(child)
            
            # Perform the initial traversal and log it
            traverse_and_log(tree)
            
            # Add edges in reversed order
            for parent_str, child_str in reversed(traversal_log):
                dot.edge(child_str, parent_str)

        # Helper function to get node name (assuming it's defined somewhere)
        def get_node_name(node):
            return str(node).split()[0]


# guides

- Check the setup: `antlr4`

- Generate the components: `antlr4 path/to/grammar.g4`

- Generate the components (include the visitor): `antlr4 path/to/grammar.g4 -visitor`

- Generate the components in python language: `antlr4 -Dlanguage=Python3 path/to/grammar.g4 -visitor`

- Install `graphviz` on linux: `conda install python-graphviz`

# references

[ANTLR](https://www.antlr.org/)

[ANTLR.lab](http://lab.antlr.org/)

[grammars-v4](https://github.com/antlr/grammars-v4)

[ANTLR4 grammar syntax support](https://marketplace.visualstudio.com/items?itemName=mike-lischke.vscode-antlr4)