class ReNameAbleClass(object):
    @classmethod
    def change_class_name(cls, new_name):
        assert new_name[0].isupper() and new_name.isalnum()
        cls.__name__ = new_name

    @classmethod
    def __str__(cls):
        return f"Class name is: {cls.__name__}"





class MyClass(ReNameAbleClass):
    pass;

myObject = MyClass()
myObject.change_class_name("SsefuClass");
print(myObject)
"""
import string

def check(new_name):
    if new_name[0] not in string.ascii_uppercase:
        return False
    for letter in new_name:
        if letter not in string.ascii_letters+string.digits:
            return False
    return True

def class_name_changer(cls, new_name):
    if check(new_name):
        cls.__name__ = new_name
    else:
        raise Exception('error')

class MyClass:
    pass

myObject = MyClass()
class_name_changer(MyClass, "UsefulClass")
print ("%s" % type(myObject).__name__)

#print(string.ascii_letters+string.digits)


"""