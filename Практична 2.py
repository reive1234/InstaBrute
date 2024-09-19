Name = [16, 'hello world','Андрій', 'лящук']
name2 = [type(x) for x in name]
print(name2)

s = 0
i = 0
f = 0
bo = 0
for x in name:
    if type(x) == str:
        s += 1
    elif type(x) == int:
        i += 1
    elif type(x) == float:
        f += 1
    elif type(x) == bool:
        bo += 1

if s>i and s>f and s>bo:
    print("STR найбільше")
elif i>s and i>f and i>bo:
    print("INT найбільше")
elif f>s and f>i and f>bo:
    print("FLOAT найбільше")
elif bo>s and bo>f and bo>i:
    print("BOOL найбільше")
    


