class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self,other):
        common = intSet()
        for i in self.vals:
            if other.member(i):
                common.insert(i)
        return common

    def __len__(self):
        return len(self.vals)


h = intSet()
h.insert(8)
h.insert(9)
h.insert(10)
h.insert(5)

m = intSet()
m.insert(3)
m.insert(2)
m.insert(7)
m.insert(8)

print(h)
print(m)
print(h.__len__())

print(m.intersect(h))
