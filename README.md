# Task
# module_1.py contains the 1st part of the task
# task.py contains modules (1)-(3)
# task_1.0.py contains modules (1)-(3)*
# test.py - test for function processing from module (2)
# clouds.yaml - for connecting via API to the Openstack

# *: This fail has 2 cases of list_to_output: Several OpenStack services provide information (lists of dicts) about the resourse in input_first_arg 
# Case 1: The information is collecting from several lists of dicts into one - list_to_output
# Case 2: The informatin is collecting from the biggest list of dicts
