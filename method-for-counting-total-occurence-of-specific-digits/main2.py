class List(object):
    def count_spec_digits(self, integers_list, digits_list):
        txt = ''.join(str(elem) for elem in integers_list)
        dictTxt = dict((i, txt.count(i)) for i in txt)
        dictKeys = dictTxt.keys()
        elem = []
        for i in digits_list:
            if str(i) in dictKeys:
                elem.append((i,dictTxt[str(i)]))
            else:
                elem.append((i,0))
        return elem

l = List()
integers_list = [1, 1, 2, 3, 1, 2, 3, 4]
#integers_list = [1,2]
#integers_list = [-77, -65, 56, -79, 6666, 222]
digits_list = [1,3,7]
ret = l.count_spec_digits(integers_list, digits_list)
print(ret)