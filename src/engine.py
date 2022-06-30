import ast
from lint_warnings import cui

class Visitor(ast.NodeTransformer):
    def visit_BoolOp(self, node:ast.AST):
        fixed = node
        if cui.is_comparing_boolop(node):
            fixed = cui.fix(node)
        self.generic_visit(node)
        return fixed

if __name__ == '__main__':
    with open('samples/cui.py') as f:
        text = f.read()

    tree = ast.parse(text)
    result = Visitor().visit(tree)
    result = ast.unparse(result)
    print(result)