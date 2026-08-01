def parse(text):
    lines = text.splitlines()
    res = []
    for l in lines:
        if l.startswith('# '): res.append(f'<h1>{l[2:]}</h1>')
        else: res.append(f'<p>{l}</p>')
    return '\n'.join(res)