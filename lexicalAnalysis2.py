import re

# Token types
TOKEN_TYPES = {
    'IF': r'\bif\b',
    'THEN': r'\bthen\b',
    'ELSE': r'\belse\b',
    'ID': r'\b[A-Za-z][A-Za-z0-9]*\b',
    'NUMBER': r'\b\d+(\.\d+)?(E[+-]?\d+)?\b',
    'LT': r'\<',
    'LE': r'\<=',
    'EQ': r'==',
    'NE': r'!=',
    'GT': r'\>',
    'GE': r'\>=',
    'WHITESPACE': r'[ \t\n]+',
    'UNKNOWN': r'.'
}

# The input string
input_string = "if a < 3 then a = 3 else a = 4"

# Lexer
class Lexer:
    def __init__(self, rules, source_code):
        self.rules = rules
        self.source_code = source_code
        self.tokens = []
        
    def tokenize(self):
        while self.source_code:
            max_len = -1
            max_type = None
            max_value = None
            
            # Try to match tokens with all the rules
            for token_type, rule in self.rules.items():
                pattern = re.compile(rule)
                match = pattern.match(self.source_code)
                
                if match and len(match.group(0)) > max_len:
                    max_len = len(match.group(0))
                    max_type = token_type
                    max_value = match.group(0)
            
            if max_len == -1:
                raise ValueError("Illegal sequence at: " + self.source_code)
            
            # Append the token to the token list and remove it from source code
            if max_type != 'WHITESPACE':  # Ignore whitespace
                self.tokens.append((max_type, max_value))
            self.source_code = self.source_code[max_len:]
        
        return self.tokens

# Create a lexer
lexer = Lexer(TOKEN_TYPES, input_string)

# Tokenize the source code
tokens = lexer.tokenize()

# Print the tokens
for token in tokens:
    print(token)
