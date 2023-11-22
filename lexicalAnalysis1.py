# Define token types
TOKEN_TYPES = ('ID', 'NUMBER', 'LT', 'LE', 'EQ', 'GT', 'GE')

class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.tokens = []
        self.current = ''

    def is_letter(self, char):
        return char.isalpha()

    def is_digit(self, char):
        return char.isdigit()

    def add_token(self, token_type):
        self.tokens.append((token_type, self.current))
        self.current = ''

    def tokenize(self):
        i = 0
        while i < len(self.source_code):
            char = self.source_code[i]

            # Skip whitespace
            if char.isspace():
                i += 1
                continue

            # Identifier or keyword
            if self.is_letter(char):
                self.current = char
                i += 1
                while i < len(self.source_code) and (self.is_letter(self.source_code[i]) or self.is_digit(self.source_code[i])):
                    self.current += self.source_code[i]
                    i += 1
                self.add_token('ID')

            # Number
            elif self.is_digit(char):
                self.current = char
                i += 1
                while i < len(self.source_code) and self.is_digit(self.source_code[i]):
                    self.current += self.source_code[i]
                    i += 1
                self.add_token('NUMBER')

            # Relational operators
            elif char == '<':
                self.current = char
                i += 1
                if i < len(self.source_code) and self.source_code[i] == '=':
                    self.current += self.source_code[i]
                    self.add_token('LE')
                    i += 1
                else:
                    self.add_token('LT')

            elif char == '=':
                self.current = char
                i += 1
                if i < len(self.source_code) and self.source_code[i] == '=':
                    self.current += self.source_code[i]
                    self.add_token('EQ')
                    i += 1

            elif char == '>':
                self.current = char
                i += 1
                if i < len(self.source_code) and self.source_code[i] == '=':
                    self.current += self.source_code[i]
                    self.add_token('GE')
                    i += 1
                else:
                    self.add_token('GT')

            else:
                raise ValueError(f"Unrecognized character {char} at position {i}")

        return self.tokens

# Example usage
input_string = "if a < 3 then a = 3 else a = 4"
lexer = Lexer(input_string)
tokens = lexer.tokenize()
print(tokens)
