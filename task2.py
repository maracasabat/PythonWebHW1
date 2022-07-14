class Meta(type):
    children_number = 0

    def __new__(mcs, name, bases, namespace, *kwargs):
        instance = super().__new__(mcs, name, bases, namespace)
        instance.class_number = mcs.children_number
        mcs.children_number += 1
        return instance

    @classmethod
    def __prepare__(mcs, name, bases, *kwargs):
        return super().__prepare__(name, bases)

    def __call__(cls, *args, **kwargs):
        return super().__call__(*args, **kwargs)


Meta.children_number = 0


class Cls1(metaclass=Meta):
    def __init__(self, data):
        self.data = data


class Cls2(metaclass=Meta):
    def __init__(self, data):
        self.data = data


class Cls3(metaclass=Meta):
    def __init__(self, data):
        self.data = data


assert (Cls1.class_number, Cls2.class_number) == (0, 1)
a, b, c = Cls1(''), Cls2(''), Cls3('')
assert (a.class_number, b.class_number) == (0, 1)
# print({Meta.children_number})
