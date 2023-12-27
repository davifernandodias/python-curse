product = {
    'name': 'blue pin',
    'price': 2.5,
    'class': 'office',
}

dc = {
    key: value.upper()
    if isinstance(value,str) else value
    for key, value
    in product.items()
}

print(dc)

