# play_around_antlr

Antlr Python

# guides

- Check the setup: `antlr4`

- Generate the components: `antlr4 path/to/grammar.g4`

- Generate the components (include the visitor): `antlr4 path/to/grammar.g4 -visitor`

- Generate the components in python language: `antlr4 -Dlanguage=Python3 path/to/grammar.g4 -visitor`

- Install `graphviz` on linux: `conda install python-graphviz`

# ANTLR

        -o ___              specify output directory where all output is generated
        -lib ___            specify location of grammars, tokens files
        -atn                generate rule augmented transition network diagrams
        -encoding ___       specify grammar file encoding; e.g., euc-jp
        -message-format ___ specify output style for messages in antlr, gnu, vs2005
        -long-messages      show exception details when available for errors and warnings
        -listener           generate parse tree listener (default)
        -no-listener        don't generate parse tree listener
        -visitor            generate parse tree visitor
        -no-visitor         don't generate parse tree visitor (default)
        -package ___        specify a package/namespace for the generated code
        -depend             generate file dependencies
        -D<option>=value    set/override a grammar-level option
        -Werror             treat warnings as errors
        -XdbgST             launch StringTemplate visualizer on generated code
        -XdbgSTWait         wait for STViz to close before continuing
        -Xforce-atn         use the ATN simulator for all predictions
        -Xlog               dump lots of logging info to antlr-timestamp.log
        -Xexact-output-dir  all output goes into -o dir regardless of paths/package

# Testing and Profiling

- Barkus-Naur-Form -> **Chain-Form**

- Profiling

# references

[ANTLR](https://www.antlr.org/)

[ANTLR.lab](http://lab.antlr.org/)

[grammars-v4](https://github.com/antlr/grammars-v4)

[ANTLR4 grammar syntax support](https://marketplace.visualstudio.com/items?itemName=mike-lischke.vscode-antlr4)

[GraphvizOnline](https://dreampuf.github.io/GraphvizOnline)