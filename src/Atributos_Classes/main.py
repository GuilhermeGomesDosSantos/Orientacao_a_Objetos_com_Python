class A:
    vc = 123

# a1 = A()
# a2 = A()

# A.vc = 321
# a1.vc = 321

    # def __init__ (self):
    #     self.vc = 321

    def __init__ (self):
        pass

a1 = A()
a2 = A()

A.vc = 'Alterado'

# print(a1.__dict__)
# print(a2.__dict__)
# print(A.__dict__)


print(a1.vc)
print(a2.vc)
print(A.vc)