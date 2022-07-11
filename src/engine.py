import ast

from detection import execute
from lint_warnings import cui
from lint_warnings import ddv

from helpers import dump
class Visitor(ast.NodeTransformer):
    def visit_BoolOp(self, node:ast.BoolOp) -> ast.BoolOp:
        fixed = node
        if cui.is_comparing_boolop(node):
            fixed = cui.fix(node)
        self.generic_visit(node)
        return fixed

    def visit_FunctionDef(self, node:ast.FunctionDef) -> ast.FunctionDef:
        self.generic_visit(node)
        return ddv.fix(node)

def _pylint_main():
    FILE = 'samples/ddv_sample.py'
    codes = {
        'ddv' : 'W0102',
        'cui' : 'R1714'
    }

    enabled = ','.join([
        codes['ddv'],
        codes['cui']
    ])

    r = execute(FILE, ['--disable=all', f'--enable={enabled}', '--output-format=json'])
    return r

def _ast_main():
    with open('samples/ddv_sample.py') as f:
        text = f.read()

    tree = ast.parse(text)
    result = Visitor().visit(tree)
    result = ast.unparse(result)
    return tree, result

if __name__ == '__main__':
    tree, r = _ast_main()

