class List:
    def remove_(self, integer_list, values_list):
        return [item for item in integer_list if item not in values_list]



l = List()
integer_list =  [1, 1, 2 ,3 ,1 ,2 ,3 ,4]
values_list = [1, 3]
l.remove_(integer_list, values_list)