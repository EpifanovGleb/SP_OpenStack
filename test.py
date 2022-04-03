    overall = []
    lst = [{'a': "success", 'b': {'f': {'e': "success"}, 'c': "fail"}}, {'a': "failure"}]
    inp_second_arg = ['a']
    inp_third_arg = "u"
    answer = ""
    print("The result of the second task:\n")

    for diction in lst:
        my_diction = diction.copy()
        my_copy = inp_second_arg.copy()
        temp = len(inp_second_arg)
        i = 0
        while i < temp:
            it = inp_second_arg[i]
            try:
                my_diction[it]

            except:
                answer = 0
                break

            if i == temp - 1:
                if type(my_diction[it]) == str:
                    answer = my_diction[it]

                else:
                    answer = 0
                    break

            else:
                if type(my_diction[it]) != dict:
                    answer = 0
                    break

                my_copy.pop(0)
                my_diction = my_diction[it]
            i += 1

        if type(answer) == str:
            print(answer, end=" ")
            if answer.find(inp_third_arg) != -1:
                overall.append(dict(diction))
    print("\n\nThe result of the task:\n")
    print(overall)
