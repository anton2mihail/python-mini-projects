class Fruit:
    def __init__(self, a="Pear", b="Green", c=10):
        self._type = a
        self._color = b
        self._price = c
    def getType(self):
        return self._type
    def setType(self, stuff):
        self._type = stuff
    def descriptor(self):
        return self._type+", "+self._color+", "

fruit1 = Fruit("Apple", "Green", 12)


fruit1.setType("Orange")
print(fruit1.descriptor())
