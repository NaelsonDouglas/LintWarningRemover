import ast

from detection import execute
from lint_warnings import cui

class Visitor(ast.NodeTransformer):
    def visit_BoolOp(self, node:ast.AST) -> ast.BoolOp:
        fixed = node
        if cui.is_comparing_boolop(node):
            fixed = cui.fix(node)
        self.generic_visit(node)
        return fixed

if __name__ == '__main__':
    r = execute('samples/ddv.py')