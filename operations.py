class Ops:
    @classmethod
    def addsum(cls,a,b):
        return a+b;

    @staticmethod
    def mul(a, b):
        return a* b;

print(Ops.addsum(3,5))
print(Ops.mul(3,5))