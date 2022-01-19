def class_name_changer(cls, new_name):
    assert new_name[0].isupper() and new_name.isalnum()
    cls.__name__ = new_name