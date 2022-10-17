# def append_to_list(value,my_list):
#     my_list.append(value)
#     print(my_list)
#
# a=[1,2,3]
# append_to_list(10,a)
# append_to_list(20,a)



# Так решается проблема с дефолтным значением мо мписком и словарем !
def append_to_list(value,my_list=None):
    """
    Функция создает список
    :param value:
    :param my_list:
    :return:
    """

    if my_list is None:
        my_list=[]
    my_list.append(value)
    print(my_list)

append_to_list(10)
append_to_list(20)
append_to_list(111)


def append_to_dict(key,value,my_dict=None):

    if my_dict is None:
        my_dict={}
    my_dict[key]=value
    print(my_dict)

append_to_dict(10,100)
append_to_dict(20,111,{'a':200})
