def flt(seq, value, flSeq=[]):
    for x in seq:
        if not isinstance(x, list):
            flSeq.append(''.join(map(bin,bytearray(x,'utf8'))))
        else:
            flt(x,value, flSeq)
    return flSeq

def locate(seq, value):
    if ''.join(map(bin,bytearray(value,'utf8'))) in flt(seq, value):
        return True
    else:
        return False



print(locate(['a','b',['(1,2)','.~`../n',['e']]],'.~`../n'))


"""
test.assert_equals(locate(['a','b',['c','d',['e']]],'a'), True)
    Test.assert_equals(locate(['a','b',['c','d',['e']]],'d'), True)
    test.assert_equals(locate(['a','b',['c','d',['e']]],'e'), True)
    test.assert_equals(locate(['a','b',['c','d',['e']]],'f'), False)
    Test.assert_equals(locate(['a','b',['c','d',['e',['a','b',['c','d',['e4']]]]]],'e4'), True)
    Test.assert_equals(locate(['a','b',['c','d',['e',['a','b',['c','d',['e',['a','b',['c','d',['e4',['a','b',['c','d',['e',['a','b',['c','d',['e',['a','b',['c','d',['e14']]]]]],]]]]]]]]],]]],'e'), True)

"""