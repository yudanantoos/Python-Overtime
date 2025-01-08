class Map:
    def __init__(self, iterate):
        self.list = []
        self.__geek(iterate)

    def geek(self, iterate):
        for item in iterate:
            self.list.append(item)

    # private copy of original geek() method
    __geek = geek


class MapSubclass(Map):

    # provides new signature for geek() but
    # does not break __init__()
    def geek(self, key, value):
        for i in zip(key, value):
            self.list.append(i)

m = Map("Tes")
print(m.list)

tes = {'ok': 'ok banget'}
ms = MapSubclass(tes.keys())
print(ms.list)