class Matematiniaiveiksmai:
    @staticmethod
    def sudetis(a, b):
        return a + b

    @staticmethod
    def atimtis(x, y):
        return x-y

#taip dirbom anksciau:
#sudetis = Matematiniaiveiksmai()
#sudetis.sudetis(4,5)

#statinis metodas

sudetis = Matematiniaiveiksmai.sudetis(5, 7)
# print(sudetis)
atimtis = Matematiniaiveiksmai.atimtis(10, 2)
print(atimtis)