class ExpressionParserWithTree:
    def __init__(self, input):
        self.input = input
        self.index = 0

    def parse(self):
        tree = self.expr()
        if self.index < len(self.input):
            raise Exception("Unexpected character at: " + str(self.index))
        return tree

    def expr(self):
        """EXPR -> TERM {+ TERM}"""
        left = self.term()
        while self.peek() == '+':
            self.consume('+')
            right = self.term()
            left = ('+', left, right)
        return left

    def term(self):
        """TERM -> FACTOR {* FACTOR}"""
        left = self.factor()
        while self.peek() == '*':
            self.consume('*')
            right = self.factor()
            left = ('*', left, right)
        return left

    def factor(self):
        """FACTOR -> ( EXPR ) | digit"""
        if self.peek() == '(':
            self.consume('(')
            result = self.expr()
            self.consume(')')
            return result
        else:
            return self.digit()

    def digit(self):
        """Parse a single digit"""
        if self.peek().isdigit():
            digit = self.peek()
            self.consume(digit)
            return ('digit', int(digit))
        else:
            raise Exception("Unexpected character at: " + str(self.index))

    def peek(self):
        """Return the current character without consuming it"""
        if self.index < len(self.input):
            return self.input[self.index]
        else:
            return None

    def consume(self, char):
        """Consume the next character if it matches 'char'"""
        if self.peek() == char:
            self.index += 1
        else:
            raise Exception("Expected " + char + " but found " + self.peek())

# Example usage
parser = ExpressionParserWithTree("3+2*2+7*3")
print(parser.parse())
parser = ExpressionParserWithTree("3+2*(2+7)*3")
print(parser.parse())
