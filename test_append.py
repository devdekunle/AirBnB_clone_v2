#!/usr/bin/python3
class Ola:
    val = []
    @property
    def get_name(self):
        return Ola.val
    @get_name.setter
    def get_name(self, value):
        Ola.val = value

inst = Ola()
inst.get_name.append('hello')
x = inst.get_name
print(x)

