import numpy as np

class Point3d(object):
    def __init__(self, x=0, y=0, z=0):
        if type(x) == list:
            # if receives a list
            try:
                assert len(x) == 3
                self.coords = np.array(x+[1],dtype=np.float64)
            except:
                raise ValueError('To create a Point3d with a list it must have length 3')
        elif type(x) == tuple:
            # if receives a tuple
            try:
                assert len(x) == 3
                self.coords = np.array(list(x)+[1],dtype=np.float64)
            except:
                raise ValueError('To create a Point3d with a tuple it must have length 3')
        elif type(x) == np.ndarray:
            try:
                assert x.ndim == 1 and x.size == 4 and x[3] == 1
                self.coords = np.array(x, dtype=np.float64)
            except:
                print "ndim", x.ndim
                print "size", x.size
                print "[3]", x[3]
                raise ValueError('To create a Point3d with an np.array it must have ndim 1, size 4, and the last element must be 1')
        elif type(x) == Point3d:
            self.coords = np.array(x.coords, dtype=np.float64)
        else:
            self.coords = np.array([x,y,z,1], dtype=np.float64)

        self.iter = 0

    def copy(self):
        return Point3d(self.coords)


    def __getattr__(self, name):
        """ When the user asks for attributes x, y, or z, we return
            coords[0], [1], and [2] """
        if name == 'x':
            return self.coords[0]
        elif name == 'y':
            return self.coords[1]
        elif name == 'z':
            return self.coords[2]

    def __getitem__(self, key):
        return self.coords[key]

    def __setattr__(self, name, value):
        """ For x, y, and z sets coords[0], [1], and [2].
            For everything else does the normal set. """
        if name == 'x':
            self.coords[0] = value
        elif name == 'y':
            self.coords[1] = value
        elif name == 'z':
            self.coords[2] = value
        else:
            self.__dict__[name] = value

    def __setitem__(self, key, value):
        self.coords[key] = value

    def __repr__(self):
        return "Point3d({0}, {1}, {2})".format(self.x, self.y, self.z)

    def __str__(self):
        return "({0}, {1}, {2})".format(self.x, self.y, self.z)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Point3d(x,y,z)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Point3d(x,y,z)

    def __mul__(self, other):
        x = self.x * other
        y = self.y * other
        z = self.z * other
        return Point3d(x,y,z)

    def dot(self, other):
        return self.coords.dot(other.coords)

    def cross(self, other):
        a = np.array([self.x, self.y, self.z])
        b = np.array([other.x, other.y, other.z])
        c = np.cross(a,b)
        return Point3d(list(c))

    def __pos__(self):
        return self

    def __neg__(self):
        return self * -1

    def __iter__(self):
        return self

    def next(self):
        if self.iter >= self.coords.size:
            self.iter = 0
            raise StopIteration
        else:
            self.iter += 1
            return self.coords[self.iter-1]

    def __len__(self):
        pass

if __name__ == '__main__':
    print "### Testing ###"

    print "\nCreation:"
    p = Point3d()
    print "Point3d()      ->", p
    p = Point3d(1,2,3)
    print "Point3d(1,2,3) ->", p
    p = Point3d([1,2,3])
    print "Point3d([1,2,3]) ->", p
    p = Point3d((1,2,3))
    print "Point3d((1,2,3)) ->", p
    p = Point3d(np.array([1,2,3,1]))
    print "Point3d(np.array([1,2,3,1])) ->", p
    q = Point3d(p)
    print "q = Point3d(p)   ->", q
    print "q.copy() ->", q.copy()

    print "\nRepresentation:"
    print "repr(p) ->", repr(p)
    print "str(p)  ->", str(p)

    print "\nGetters:"
    print "p.x ->", p.x
    print "p.y ->", p.y
    print "p.z ->", p.z
    print "p.coords    ->", p.coords
    print "p.coords[0] ->", p.coords[0]
    print "p.coords[1] ->", p.coords[1]
    print "p.coords[2] ->", p.coords[2]
    print "p[0] ->", p[0]
    print "p[1] ->", p[1]
    print "p[2] ->", p[2]

    print "\nSetters:"
    p.x = 10
    print "p.x = 10 ->", p.x
    p.y = 10
    print "p.y = 10 ->", p.y
    p.z = 10
    print "p.z = 10 ->", p.z
    p.coords = np.array([1,2,3])
    print "# This next one is not recommended at all."
    print "p.coords = np.array([1,2,3]) ->", p
    p.coords[0] = 10
    print "p.coords[0] = 10 ->", p[0]
    p.coords[1] = 10
    print "p.coords[1] = 10 ->", p[1]
    p.coords[2] = 10
    print "p.coords[2] = 10 ->", p[2]
    p[0] = 1
    print "p[0] = 1 ->", p[0]
    p[1] = 1
    print "p[1] = 1 ->", p[1]
    p[2] = 1
    print "p[2] = 1 ->", p[2]

    print "\nOperators:"
    i = Point3d(1,0,0)
    j = Point3d(0,1,0)
    print "i = Point3d(1,0,0)\nj = Point3d(0,1,0)\n"
    print "+i ->", +i
    print "-i ->", -i
    print "i + j  ->", (i + j)
    print "i - j  ->", (i - j)
    i += j
    print "i += j ->", i
    i = Point3d(1,0,0)
    i -= j
    print "i -= j ->", i
    i = Point3d(1,0,0)
    print "i * 2  ->", i * 2
    i *= 2
    print "i *= 2 ->", i
    i = Point3d(1,0,0)
    print "i.dot(j)   ->", i.dot(j)
    print "j.dot(i)   ->", j.dot(i)
    print "i.cross(j) ->", i.cross(j)
    print "j.cross(i) ->", j.cross(i)


    print "\nIterators:"

    print "\nCoordinate Systems:"

    print "\nTransformations:"











