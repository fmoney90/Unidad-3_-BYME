


"""    BERNARD Yves Mary Emmanuel
       CODE : 1215101007
       Prototype Exemple
"""




import copy


class Prototype:
    def __int__(self):
        self._objects = {}

    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Unregister an object"""
        del self.object[name]

    def clone(self, name, **attr):
        """clone a registered object and update its attributes"""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


class Car:
    def __init__(self):
        self.name = "Skylark"
        self.color = "Red"
        self.options = "Ex"

    def __str__(self):
        return '{}|{}|{}|'.format(self.name, self.color, self.options)


c = Car()
prototype = Prototype()
prototype.register_object('skylark',c)

c1 = prototype.clone('skylark')

print(c1)