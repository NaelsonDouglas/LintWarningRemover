import sys

def base_hasher(key):
    tokens = enumerate(map(ord, key))
    result = ''
    for position, token in tokens:
        result = result+chr(position+token+len(result))
    return result.replace('\n',' ')

print(base_hasher(sys.argv[1]))