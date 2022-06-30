import ast
from lint_warnings import cui

no = None

def test_srs(src:str):
    return ast.dump(ast.parse(src, mode='eval'), indent=4)


if __name__ == '__main__':
    with open('samples/cui.py') as f:
        text = f.read()

    for node in ast.walk(ast.parse(text)):
        if type(node) == ast.BoolOp:
            if len(node.values) > 2:
                no = node
                d = ast.dump(no, indent=4)
                print(d)
                print(10*'-')
            if cui.is_comparing_boolop(node):
                fixed = cui.fix(node)
                print('comparou')