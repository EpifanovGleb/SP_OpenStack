def processing(x):
    answer = ""
    for it in x:
        if type(x[it]) != dict:
            return x[it]
        else:
            answer = processing(x[it])

    return answer


lst = [{'a': {'b': {'c': "fail"}}}, {'c': 'd'}, {'b': {'c': "fail"}}]

while True:
    data = dict()
    try:
        key = input()
        value = input()
    except:
        break
    data[key] = value
    lst.append(data)

for diction in lst:
    for i in diction:
        if type(diction[i]) != dict:
            result = diction[i]
        else:
            result = processing(diction[i])
        print(result)
