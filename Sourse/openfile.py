def open_in(x):
    f = open(x, 'r', encoding='Utf-8')
    text = f.read()
    f.close()
    return text


