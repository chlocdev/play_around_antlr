import time
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from antlr4.error.ErrorListener import ErrorListener

class ProfilingErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.ambiguities = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if isinstance(e, RecognitionException) and e.offendingState is not None:
            # Capture ambiguity information
            self.ambiguities.append((line, column, msg))

    def get_ambiguities(self):
        return self.ambiguities


class ProfilingListener(ParseTreeListener):
    def __init__(self):
        self.rule_invocations = {}
        self.rule_times = {}
        self.total_time = 0.0  # Variable to accumulate total time across all rules
        self.start_time = None
        self.current_rule = None

    def enterEveryRule(self, ctx):
        rule_name = ExprParser.ruleNames[ctx.getRuleIndex()]
        if rule_name not in self.rule_invocations:
            self.rule_invocations[rule_name] = 0
            self.rule_times[rule_name] = 0.0
        self.rule_invocations[rule_name] += 1
        self.current_rule = rule_name
        self.start_time = time.time()

    def exitEveryRule(self, ctx):
        if self.start_time is not None:
            end_time = time.time()
            elapsed_time = end_time - self.start_time
            self.total_time += elapsed_time
            self.rule_times[self.current_rule] += elapsed_time
            self.start_time = None
            self.current_rule = None

    def get_profiling_info(self):
        return self.rule_invocations, self.rule_times, self.total_time


class ProfilingParser(ExprParser):
    def __init__(self, input_stream):
        super().__init__(input_stream)
        self.decision_count = 0
        self.max_lookahead = 0
        self.lookahead_counts = []
        self.error_listener = ProfilingErrorListener()
        self.addErrorListener(self.error_listener)

    def getDecisionCount(self):
        return self.decision_count

    def getMaxLookahead(self):
        return self.max_lookahead

    def getLookaheadCounts(self):
        return self.lookahead_counts

    def get_ambiguities(self):
        return self.error_listener.get_ambiguities()

    def consume(self):
        self.decision_count += 1
        super().consume()

    def match(self, ttype):
        self.decision_count += 1
        return super().match(ttype)

    def recover(self, e):
        self.decision_count += 1
        super().recover(e)

    def getLookahead(self):
        self.lookahead_counts.append(self._interp._decisionToDFA)
        current_lookahead = max(len(dfa) for dfa in self.lookahead_counts)
        self.max_lookahead = max(self.max_lookahead, current_lookahead)
        return super().getLookahead()


def generate_profiling_info(input_stream):
    
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ProfilingParser(stream)
    
    tree = parser.prog()

    profiling_listener = ProfilingListener()
    walker = ParseTreeWalker()
    walker.walk(profiling_listener, tree)

    rule_invocations, rule_times, total_time = profiling_listener.get_profiling_info()

    print("Rule Invocations:")
    for rule, count in rule_invocations.items():
        print(f"{rule}: {count} times")
    
    print("\nRule Execution Times:")
    for rule, total_time in rule_times.items():
        print(f"{rule}: {total_time:.6f} seconds")

    print(f"\nTotal Time: {total_time:.6f} seconds")

    # Print total number of decisions made
    total_decisions = parser.getDecisionCount()
    print(f"\nTotal Decisions: {total_decisions}")

    # Print maximum lookahead depth
    max_lookahead = parser.getMaxLookahead()
    print(f"Max Lookahead Depth: {max_lookahead}")

    # Print ambiguities
    ambiguities = parser.get_ambiguities()
    print("\nAmbiguities:")
    for ambiguity in ambiguities:
        print(f"Line {ambiguity[0]}, Column {ambiguity[1]}: {ambiguity[2]}")


if __name__ == "__main__":
    input_str = """a = 3 + 4 * 5
    b = (a - 2) / 3
    """
    input_stream = InputStream(input_str)
    generate_profiling_info(input_stream)
