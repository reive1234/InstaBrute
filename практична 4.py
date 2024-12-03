valume = [3, 1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 6, 5, 4, 3, 4, 5, 4, 3, 'Привіт', 'анаконда']
sorted_compilation = []
int_ = []
str_ = []
def test(function):
    for element in function:
        if element not in sorted_compilation:
            sorted_compilation.append(element)
    for element in sorted_compilation:
        if type(element) == int:
            int_.append(element)
        elif type(element) == str:
            str_.append(element)
            #сорт. по інт і стр
    int_.sort()
    str_.sort()
    return int_ + str_
result = test(valume) # виз. функ.
print("Відсортований список:", result)
