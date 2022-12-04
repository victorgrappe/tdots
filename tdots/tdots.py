
from tdots.tdot import Tdot
class Tdots():

    def __init__(self, all={}):
        self.all = all

    def __str__(self):
        return f"Tdots()"

    def create(self, tdot: Tdot):
        self.all[tdot.key] = tdot

    def read(self, key):
        return self.all[key]

    def update(self, tdot):
        self.all[tdot.key] = tdot

    def delete(self, key):
        self.all.pop(key)