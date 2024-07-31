In ANTLR, `RecognitionException` and `NoViableAltException` are exception classes used for error handling during the parsing process. They are part of the ANTLR runtime library and help manage and report errors encountered while parsing input according to the defined grammar. Here's an overview of these exceptions:

### `RecognitionException`

**`RecognitionException`** is the base class for exceptions that occur during parsing when the parser fails to recognize valid input according to the grammar rules.

#### Key Points:

1. **Base Class**:
   - `RecognitionException` is a base class for various specific parsing exceptions. It provides a general mechanism for handling errors that arise when the parser encounters input that does not match the expected grammar rules.

2. **Purpose**:
   - It is used to signal any type of error in the recognition process, such as syntax errors, token mismatches, or unexpected input.

3. **Attributes and Methods**:
   - `RecognitionException` typically contains information about the position of the error in the input stream and the specific parser rule where the error occurred.
   - It provides methods for getting the line and character position of the error, as well as for retrieving the input stream that caused the error.

4. **Usage**:
   - Handlers for `RecognitionException` are used to provide error messages or corrective actions when parsing fails. This can include logging errors, reporting them to the user, or attempting to recover from the error.

**Example Usage**:

```python
def some_rule(self):
    try:
        # Parsing logic
        pass
    except RecognitionException as e:
        print("Recognition error:", e)
        self._errHandler.reportError(self, e)
        self._errHandler.recover(self, e)
```

### `NoViableAltException`

**`NoViableAltException`** is a specific subclass of `RecognitionException` that is thrown when the parser encounters an input that does not match any of the alternatives available for a specific grammar rule.

#### Key Points:

1. **Specific Exception**:
   - `NoViableAltException` is thrown when the parser cannot find a valid alternative to continue parsing. This typically occurs when the input does not fit any of the options specified in the grammar rules for a given parsing state.

2. **Purpose**:
   - It is used to handle situations where the parser has exhausted all possible parsing options for a rule and found that none of them fit the input.

3. **Attributes and Methods**:
   - Provides details about the specific rule where the error occurred and the alternatives that were considered.
   - Can also include information about the token that caused the error and the state of the parser when the error was detected.

4. **Usage**:
   - Handlers for `NoViableAltException` typically involve logging detailed error messages or attempting to recover from the error. It helps in debugging parsing issues and understanding why a particular input failed to match any expected alternatives.

**Example Usage**:

```python
def some_rule(self):
    try:
        # Parsing logic
        pass
    except NoViableAltException as e:
        print("No viable alternative error:", e)
        self._errHandler.reportError(self, e)
        self._errHandler.recover(self, e)
```

### Summary

- **`RecognitionException`**: A general exception class for all parsing errors. It serves as the base class for more specific parsing errors and provides basic error handling functionality.

- **`NoViableAltException`**: A specific subclass of `RecognitionException` that indicates a failure to match any of the viable alternatives for a parsing rule. It provides detailed information about why the parser could not proceed with any alternative.

Both exceptions are crucial for understanding and managing errors during parsing, allowing you to handle and recover from syntax errors and other issues that arise when processing input according to the defined grammar.