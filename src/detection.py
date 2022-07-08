import pandas as pd
from pylint import lint
from pylint.reporters.text import TextReporter

import parse

class DummyWritable():
    def __init__(self):
        self.content = []

    def write(self, stream):
        self.content.append(stream)

    def read(self):
        return self.content

def _parse(matches:list) -> list:
    format = '{file}:{line}:{col}: {code}: {warning} ({msg})'
    result = [parse.parse(format, m) for m in matches]
    result = [r.named for r in result if r is not None]
    return pd.DataFrame(result)

def execute(filename:str, args:list=None) -> list:
    if not args:
        args = []
    _cmd = [filename]+args
    pylint_output = DummyWritable()
    lint.Run(_cmd, reporter=TextReporter(pylint_output), exit=False)
    return _parse(pylint_output.read())
