from datetime import datetime

class CustomMap:
    def __init__(self):
        self.hashmap = {}
        self.validIndexes = {}
        self.setAllValue = None
        self.lastChange = 0

    def set(self, key, value):
        self.hashmap[key] = value
        self.validIndexes[key] = datetime.now().timestamp()

    def get(self, key):
        if self.lastChange < self.validIndexes[key]:
            return self.hashmap[key]
        else:
            return self.setAllValue

    def setAll(self, value):
        self.setAllValue = value
        self.hashmap = {}
        self.lastChange = datetime.now().timestamp()

d = CustomMap()
d.set(1,3)
d.set(2,4)
d.set(3,6)
print(d.get(1))
print(d.get(2))
print(d.get(3))
print('')
d.setAll(5)
print(d.get(1))
print(d.get(2))
print(d.get(3))
print('')
d.setAll(7)
print(d.get(1))
print(d.get(2))
print(d.get(3))
print('')
d.set(2,4)
d.set(3,8)
print(d.get(1))
print(d.get(2))
print(d.get(3))