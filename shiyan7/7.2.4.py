import math

class Vector:
    def __init__(self, components):
        self.components = components

    def __str__(self):
        return '(' + ', '.join(map(str,self.components)) + ')'

    def __len__(self):
        return len(self.components)

    def add(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must be of the same length")
        return Vector([x + y for x, y in zip(self.components,other.components)])

    def sub(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must be of the same length")
        return Vector([x - y for x, y in zip(self.components,other.components)])

    def dot(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must be of the same length")
        return sum(x * y for x, y in zip(self.components,other.components))

    def norm(self):
        return math.sqrt(sum(x ** 2 for x in self.components))

    def equals(self, other):
        return self.components == other.components
a = Vector([1,2])
b = Vector([3,4])
print(a.add(b))