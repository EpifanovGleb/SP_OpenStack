import openstack
import sys
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
    tmp = []
    for x in tmp_list:
        tmp.append(string_parsing(x))
    answer_list = tmp
    for y in tmp:
        if y.find("v2") != -1:
            answer_list.append(y.replace("v2", ""))
        if y.find("v3") != -1:
            answer_list.append(y.replace("v3", ""))

    my_set = set(answer_list)
    answer_list = list(my_set)
    return answer_list


if __name__ == '__main__':
    inp_first_arg = ""
    inp_second_arg = []
    inp_third_arg = ""

    for i, arg in enumerate(sys.argv):  # Parsing command line
        if i == 1:
            inp_first_arg = arg
        else:
            if 1 < i < len(sys.argv) - 1:
                inp_second_arg.append(arg)
            if i == len(sys.argv) - 1:
                inp_third_arg = arg

    flag_task_3 = False
    if len(inp_second_arg) == 0 and inp_third_arg == "":
        flag_task_3 = True

    conn = openstack.connect(cloud='openstack', region_name='regionOne')  # Connecting to OpenStack
    list_of_available_services = []

    my_dict = conn.service_catalog  # Getting the list of available services
    for element in my_dict:
        temp = element.get("type")  # Parsing the dicts -> getting a list of available services
        list_of_available_services.append(temp)

    list_of_available_services = processing(list_of_available_services)  # Changing the list
    #list_of_available_services.remove("key_manager")
    print("The list of available services (refactored):\n")
    print(list_of_available_services, "\n")

    list_to_output = []
    tmp_vec = []
    counter = False

    for elem in list_of_available_services:
        if elem == 'key_manager':
            print("WARNING!: The key-manager service for openstack:regionOne exists but does not have any supported versions.")
        else:
            flag = True
            if hasattr(conn, elem):
                my_object = getattr(conn, elem)
                dict_my = []

                try:
                    dict_my = getattr(my_object, inp_first_arg)
                except:
                    flag = False
                    print("WARNING!: The service", elem, "hasn't got any information about - ", inp_first_arg, "resource")
                if flag:
                    dict_my = getattr(my_object, inp_first_arg)

                    print("CONGRATS! We have any info about", inp_first_arg, "resource via service - ", elem)
                    if counter:
                        tmp_dict = list(list_to_output[0].keys())
                        i = 0
                        for it in dict_my():
                            for el in it:
                                if list_to_output[i].get(el) == None:
                                    list_to_output[i].update({el: it.get(el)})
                            i += 1
                    else:
                        try:
                            for it in dict_my():
                                list_to_output.append(dict(it))
                            counter = True
                        except:
                            print("ACCESS ERROR: You are not authorized to perform the requested action: identity:list_", inp_first_arg, sep="")



    print("\n")
    if flag_task_3:
        print("OPTIONAL MODE: PRINTING EVERYTHING about", inp_first_arg, "resource:\n")
        if len(list_to_output) == 0:
            print("NOTHING TO SHOW")
        else:
            pprint(list_to_output)
    else:
        print("DEFAULT MODE OF THE TASK:\n")
        if len(list_to_output) == 0:
            print("Nothing to output")
        else:
            overall = []  # Final list to output
            check_for_key = True
            for diction in list_to_output:
                if check_for_key == 0:
                    break
                else:
                    answer = ""
                    my_diction = diction.copy()
                    my_copy = inp_second_arg.copy()
                    temp = len(inp_second_arg)
                    i = 0
                    while i < temp:
                        it = inp_second_arg[i]
                        try:
                            my_diction[it]
                        except:
                            print("WARNING!: No such key\n")
                            answer = 0
                            check_for_key = False
                            break

                        if i == temp - 1:
                            if type(my_diction[it]) == str:
                                answer = my_diction[it]

                            else:
                                answer = 0
                                break

                        else:
                            if type(my_diction[it]) == str or type(my_diction[it]) == list:
                                answer = 0
                                break

                            my_copy.pop(0)
                            my_diction = my_diction[it]
                        i += 1

                    if type(answer) == str:
                        print(answer, end=" ")
                        if answer.find(inp_third_arg) != -1:
                            overall.append(dict(diction))
            if len(overall) == 0:
                print("No one substring were found")
            else:
                print("\n\nThe result of the task:\n")
                pprint(overall[0])










