import openstack
from openstack import connection, orchestration
from keystoneauth1 import loading
from keystoneauth1 import session as session
from keystoneclient.v3 import client as client
from keystoneauth1.identity import v3
import openstack.compute.v2.limits
from keystoneauth1 import loading
from keystoneauth1 import session


def processing(x):
    answer = ""
    for it in x:
        if type(x[it]) != dict:
            return x[it]
        else:
            answer = processing(x[it])

    return answer


conn = openstack.connect(cloud='openstack', region_name='regionOne')  # Getting an object after call

''' #Another way to connect
loader = loading.get_plugin_loader('password')
auth = loader.load_from_options(auth_url='https://sky.ispras.ru:13000',
                                username='epifanov',
                                 password='GlebEpifanov6354',
                                 project_id='b71e624e352e46979b4ed9fff16759dc',
                                user_domain_name="Default")


data = openstack.compute.v2.limits.AbsoluteLimits(session=conn)
print(data.to_dict())
conn.get_compute_quotas("users")
'''

# # # Module 1

input_first_arg = input()  # The input of a first str

# CASE 1
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

# CASE 2
'''
check_string = "list_" + input_first_str
flag_3 = hasattr(conn, check_string)
if flag_3:
    my_dict = getattr(conn, check_string)
    pprint(my_dict())
'''

# # # Module 2 and 3


# Case of manual input
'''
lst = []
while True:
    data = dict()
    try:
        key = input()
        value = input()
    except:
        break
    data[key] = value
    lst.append(data)
print(lst)
'''
print("\nThe result:\n")


lst = [{'a': {'b': {'c': "fail"}}}, {'c': 'd'}, {'b': {'c': "fail"}}]
inp_third_arg = input()
for diction in lst:
    for i in diction:
        if type(diction[i]) != dict:
            result = diction[i]
        else:
            result = processing(diction[i])
        # print(result) # Printing the result of processing function

        if result.find(inp_third_arg) != -1:
            print("{'", i, "': ", diction[i], "}", sep="")





