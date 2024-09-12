
a = [52, 'hello world', 3.14, True, [1, 2, 3], (4, 5), None, 100, ]

b = [type(a) for a in a]

c = max(set(b), key=b.count)

print(f"Найчастіше зустрічається тип даних: {c}")