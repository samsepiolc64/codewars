class List(object):
    def count_spec_digits(self, integers_list, digits_list):
        txt = ''.join(str(e) for e in integers_list)
        dictTxt = dict((i,0) for i in digits_list)
        for i in list(map(str, digits_list)):
            if i in txt:
                dictTxt[int(i)] = txt.count(i)
        pack = [(i,dictTxt[i]) for i in dictTxt]
        return pack


l = List()
#integers_list = [1, 1, 2, 3, 1, 2, 3, 4]
#integers_list = []
integers_list = [-77, -65, 56, -79, 6666, 222]

digits_list = [5,3]
ret = l.count_spec_digits(integers_list, digits_list)
print(ret)