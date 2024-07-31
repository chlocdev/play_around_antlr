To measure the maximum amount of lookahead tokens used in a single decision for a rule in an ANTLR parser, you need to customize the ANTLR runtime. This involves tracking the lookahead tokens used during parsing decisions. Here's how you can achieve this in Python:

### Steps to Measure Maximum Lookahead Tokens

1. **Subclass the Parser and ATN Simulator**

   You need to subclass the `Parser` and possibly the `ParserATNSimulator` to monitor and track the lookahead tokens used during decisions.

2. **Modify the Grammar File**

   Use ANTLR to generate the parser and lexer from your grammar file.

3. **Use Your Custom Parser in Code**

   Implement your custom parser and lexer in your application.

Here’s a detailed guide:

### 1. Subclass the Parser and ATN Simulator

**Custom `Parser` and `ParserATNSimulator` Classes**

You will create a custom parser and ATN simulator to track the maximum lookahead tokens used.

1. **Create Custom Parser Class**

   Subclass the `Parser` class to keep track of the maximum lookahead tokens used.

   ```python
   from antlr4 import Parser
   from antlr4.ParserATNSimulator import ParserATNSimulator
   from antlr4.TokenStreamRewriter import TokenStreamRewriter

   class CustomParser(Parser):
       def __init__(self, *args, **kwargs):
           super().__init__(*args, **kwargs)
           self.max_lookahead_tokens = 0
           self._interp = CustomParserATNSimulator(self, self._atn, self._decisionToDFA, self._sharedContextCache)

       def get_max_lookahead_tokens(self):
           return self.max_lookahead_tokens
   ```

2. **Create Custom ATN Simulator Class**

   Subclass the `ParserATNSimulator` to track lookahead tokens during parsing decisions.

   ```python
   from antlr4.ParserATNSimulator import ParserATNSimulator

   class CustomParserATNSimulator(ParserATNSimulator):
       def __init__(self, parser, atn, decisionToDFA, sharedContextCache):
           super().__init__(parser, atn, decisionToDFA, sharedContextCache)
           self.max_lookahead_tokens = 0

       def adaptivePredict(self, input, decision, outerContext):
           lookahead = super().adaptivePredict(input, decision, outerContext)
           self.max_lookahead_tokens = max(self.max_lookahead_tokens, len(input.getTokens()))
           return lookahead

       def get_max_lookahead_tokens(self):
           return self.max_lookahead_tokens
   ```

3. **Update the Grammar File**

   Generate the lexer and parser from your grammar file using ANTLR.

   ```bash
   antlr4 -Dlanguage=Python3 YourGrammar.g4
   ```

4. **Use Your Custom Parser in Your Code**

   Instantiate and use your custom parser in your application code.

   ```python
   from antlr4 import InputStream
   from YourGrammarLexer import YourGrammarLexer
   from YourGrammarParser import CustomParser  # Import your custom parser

   def main():
       lexer = YourGrammarLexer(InputStream("your input text"))
       stream = CommonTokenStream(lexer)
       parser = CustomParser(stream)

       # Parse with your rule
       tree = parser.yourRule()

       # Retrieve the maximum lookahead tokens
       print(f"Max lookahead tokens used: {parser.get_max_lookahead_tokens()}")

   if __name__ == "__main__":
       main()
   ```

### 2. Verify and Test

Run your parser with the custom lexer and parser to ensure that the maximum lookahead tokens are correctly tracked and reported.

### Additional Notes

- **ANTLR Version**: Ensure compatibility with your version of ANTLR. Modify the code as needed based on the version and runtime changes.
- **Complexity**: Customizing the runtime requires a deep understanding of ANTLR’s internal mechanisms. Thorough testing is essential to ensure correctness.
- **Documentation and Community**: Refer to the [ANTLR documentation](https://github.com/antlr/antlr4) and community forums for additional information and support.

By following these steps, you can measure the maximum number of lookahead tokens used in a single decision for a rule, which provides insights into the complexity and efficiency of your grammar.