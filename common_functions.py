"""
Is used to store reusable functions
"""

import collections
import re


com_menu_confirm = collections.OrderedDict([("1", "Confirm"), ("0", "Cancel")])


def menu_handling(dictionary, separator, sub=0):
    """
    Is used to handle the hierarchy menu from dictionary
    :param dictionary:
    :param separator:
    :param sub:
    :return:
    """
    match sub:
        case 0:
            print(", ".join(str(key) + separator + str(value) for key, value in dictionary.items()))
        case 1:
            print(", ".join(str(key) + separator + str(value["label"])
                            for key, value in dictionary.items()))
    while True:
        action = input("Please, select an action: ")
        if action in dictionary.keys():
            break
    match sub:
        case 0:
            return action
        case 1:
            return (action, dictionary.get(action))


def var_input_validate(target_type, input_tip="Please, input the value: ", stop_key="stop"):

    """allowed types : "int", "float", "str", "boolean"
    Is used to convert the input to the appropriate defined type.
    The output value type would be equal to inputted type in case it is possible.
    Otherwise, the error will be returned."""

    allowed_types = ['int', 'float', 'str', 'bool']
    converted_value = None
    if target_type in allowed_types:
        while True:
            x = input(input_tip.rpartition(':')[0] + "(stop key: " + stop_key + "): ")
            if x != stop_key:
                try:
                    converted_value = eval(target_type + '("' + x + '")')
                    return converted_value
                except ValueError:
                    print("Was expected the type {0} as an input.".format(target_type))
                except NameError:
                    print("Was expected the type {0} as an input.".format(target_type))
            else:
                return converted_value
    else:
        print("The received type is not supported the list of allowed types is: "
              + str(allowed_types))
        return converted_value


def float_range(end, start=0.0, step=1.0):
    """
    Is used to generate float range with start/stop and step
    :param end:
    :param start:
    :param step:
    :return:
    """
    l_range = []
    cur_element = start
    while cur_element < end:
        cur_element += step
        l_range.append(cur_element)
    return list(l_range)


def dict_insert_update(dictionary, action="insert", input_key=None, use_value_as_key=False,
                       key_tip="Please, input the key", value_tip="Please, input the value"):
    """

    :param dictionary:
    :param action:
    :param input_key:
    :param use_value_as_key:
    :param key_tip:
    :param value_tip:
    :return:
    """
    if use_value_as_key:
        value = input(value_tip)
        key = re.sub(r"\W", "", value)
    elif input_key:
        key = input_key
        value = input(value_tip)
    else:
        key = input(key_tip)
        value = input(value_tip)
    if action == "insert" and key in dictionary:
        print("Record with provided key exists. Do You want to replace it with new value?")
        if menu_handling(com_menu_confirm, "-") == "2":
            return key
    elif action in ["update", "insert"]:
        dictionary.update({key: value})
    return key


def dict_sort(dictionary, sort_by="key", order_asc=True):
    """
    :param dictionary:
    :param sort_by:
    :param order_asc:
    :return:
    """
    match sort_by:
        case "key":
            sorted_dict = sorted(dictionary.items(), reverse=not order_asc)
        case "value":
            sorted_dict = sorted(dictionary.items(),
                                 reverse=not order_asc,
                                 key=lambda item: item[1])
    return sorted_dict
