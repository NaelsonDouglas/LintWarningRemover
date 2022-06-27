import ast
no = None

def cui_fix(node:ast.BoolOp):
    assert isinstance(node.op, ast.Or)
    return None

def is_comparing(node:ast.BoolOp, left_name:str):
    assert isinstance(node, ast.BoolOp)
    assert isinstance(node.op, ast.Or)
    if len(node.values) > 1:
        comparing = {value for value in node.values if isinstance(value, ast.Compare)}
        not_comparing = set(node.values) - comparing
        comparing = list(comparing)

        _ids = {c.left.id for c in comparing}
        maped_comparisons = dict([(_id, set()) for _id in _ids])
        for comparison in comparing:
            assert len(comparison.comparators) == 1
            maped_comparisons[comparison.left.id].add(comparison.comparators[0].value)
        breakpoint()
        comparisons
    else:
        return False


if __name__ == '__main__':
    with open('samples/cui.py') as f:
        text = f.read()
    tree = ast.parse(text)

    for node in ast.walk(tree):
        # print(node)
        if type(node) == ast.BoolOp and len(node.values) > 2:
            no = node
        if isinstance(node, ast.BoolOp) and is_comparing(node, 'value'):
            print('comparou')
    # print(ast.dump(no, indent=4))