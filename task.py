import openstack
from openstack import connection, orchestration
from keystoneauth1 import loading
from keystoneauth1 import session as session
from keystoneclient.v3 import client as client
from keystoneauth1.identity import v3
import openstack.compute.v2.limits
from keystoneauth1 import loading
from keystoneauth1 import session
from pprint import pprint


def processing(x, lst_1):
    answer = 0
    for it in x:
        if it == lst_1[0]:
            if type(x[it]) == str:
                if len(lst_1) == 1:
                    return x[it]
                else:
                    return 0
            if type(x[it]) == dict:
                if len(lst_1) > 1:
                    lst_1.pop(0)
                    answer = processing(x[it], lst_1)
                else:
                    return 0

        return answer


if __name__ == '__main__':

    conn = openstack.connect(cloud='openstack', region_name='regionOne')  # Getting an object after call
# # # Module 1

input_first_arg = ""  # The input of a first str

# CASE 1
'''
flag_1 = hasattr(conn.compute, input_first_arg)  # Checking if attribute exists
if flag_1:
    my_dict = getattr(conn.compute, input_first_arg)  # If attribute exists
    for temp in my_dict():
        print(temp.name)

flag_2 = hasattr(conn.identity, input_first_arg)
if flag_2:
    my_dict = getattr(conn.identity, input_first_arg)  # If attribute exists
    for temp in my_dict():
        print(temp)

'''
# CASE 2
'''
my_dict = {}
check_string = "list_" + input_first_arg
conn.list_stacks()

flag_3 = hasattr(conn, check_string)
if flag_3:
    my_dict = getattr(conn, check_string)
    pprint(my_dict())
# # # Module 2 and 3
my_lst = []
while True:
    try:
        key = input()
    except:
        break
    my_lst.append(key)
print(my_lst)
'''

lst = [{'a': "success", 'b': {'f': {'e': "success"}, 'c': "fail"}}, {'a': "failure"}]
inp_second_arg = ['a']
inp_third_arg = "r"
answer = ""

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
    #print(answer)
    if type(answer) == str:
        if answer.find(inp_third_arg) != -1:
            print(diction)








