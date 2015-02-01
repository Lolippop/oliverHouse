class Person(object):
    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age = age

    def print_name(self):
        print '%d: %s' % (self.id, self.name)
