import openstack
from pprint import pprint


def string_parsing(tmp_str):
    result = tmp_str
    while True:
        checker = result.find('-')
        if checker != -1:
            result = result.replace("-", "_")  # For example: key-manager -> key_manager
        else:
            break
    return result


def processing(tmp_list):
    list_for_check = ['volume']
    answer = []
    for y in tmp_list:
        answer.append(string_parsing(y))

    for z in list_for_check:
        for x in tmp_list:
            if x.find(z):
                answer.append(z)
                break

    return answer


if __name__ == '__main__':
    conn = openstack.connect(cloud='openstack', region_name='regionOne')
    input_first_arg = "images"
    list_of_available_services = []

    my_dict = conn.service_catalog  # Getting the list of available services
    for element in my_dict:
        temp = element.get("type")
        list_of_available_services.append(temp)

    list_of_available_services = processing(list_of_available_services)  # Changing the list
    list_of_available_services.remove("key_manager")
    print(list_of_available_services)

    counter = False
    #list_of_available_services = ['volumev3', 'baremetal_introspection', 'cloudformation', 'compute', 'image', 'network', 'orchestration', 'baremetal', 'object_store', 'placement', 'identity', 'volumev2', 'volume']
    list_to_output = []
    tmp_vec = []

    for elem in list_of_available_services:
        flag = True
        if hasattr(conn, elem):
            my_object = getattr(conn, elem)
            dict_my = []
            try:
                dict_my = getattr(my_object, input_first_arg)
            except:
                flag = False

            if flag:
                dict_my = getattr(my_object, input_first_arg)
                #print(elem)
                if counter:
                    tmp_dict = list(list_to_output[0].keys())
                    i = 0
                    for it in dict_my():
                        for el in it:
                            if list_to_output[i].get(el) == None:
                                list_to_output[i].update({el: it.get(el)})

                        i += 1
                else:
                    check = True
                    try:
                        for it in dict_my():  # groups
                            list_to_output.append(dict(it))
                        counter = True
                    except:
                        check = False

    pprint(list_to_output, sort_dicts=False)




