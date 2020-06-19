import  numpy as np
def locate(seq, value):
    while True:
        print(seq)
        seq = np.concatenate(seq, axis=None)
        if all(isinstance(x, str) for x in seq):
            break
    if value in seq:
        return True
    else:
        return False







print(locate(['a','b',['c','d',['e',['a','b',['c','d',['e4']]]]]],'es4'))


"""
test.assert_equals(locate(['a','b',['c','d',['e']]],'a'), True)
    Test.assert_equals(locate(['a','b',['c','d',['e']]],'d'), True)
    test.assert_equals(locate(['a','b',['c','d',['e']]],'e'), True)
    test.assert_equals(locate(['a','b',['c','d',['e']]],'f'), False)
    Test.assert_equals(locate(['a','b',['c','d',['e',['a','b',['c','d',['e4']]]]]],'e4'), True)
    Test.assert_equals(locate(['a','b',['c','d',['e',['a','b',['c','d',['e',['a','b',['c','d',['e4',['a','b',['c','d',['e',['a','b',['c','d',['e',['a','b',['c','d',['e14']]]]]],]]]]]]]]],]]],'e'), True)

"""