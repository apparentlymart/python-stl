

class Solid(object):

    def __init__(self, name=None, facets=None):
        self.name = name
        self.facets = facets if facets is not None else []

    def add_facet(self, *args, **kwargs):
        self.facets.append(Facet(*args, **kwargs))

    def __eq__(self, other):
        if type(other) is Solid:
            if self.name != other.name:
                return False
            if len(self.facets) != len(other.facets):
                return False
            for i, self_facet in enumerate(self.facets):
                if self_facet != other.facets[i]:
                    return False
            return True
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return '<stl.types.Solid name=%r, facets=%r>' % (
            self.name,
            self.facets,
        )


class Facet(object):

    def __init__(self, normal, vertices):
        self.normal = normal
        self.vertices = tuple(vertices)
        if len(self.vertices) != 3:
            raise ValueError('Must pass exactly three vertices')

    def __eq__(self, other):
        if type(other) is Facet:
            return (
                self.normal == other.normal and
                self.vertices == other.vertices
            )
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return '<stl.types.Facet normal=%r, vertices=%r>' % (
            self.normal,
            self.vertices,
        )

class Vector3d(tuple):

    def __new__(cls, x, y, z):
        return tuple.__new__(cls, (x, y, z))

    def __init__(self, x, y, z):
        pass

    @property
    def x(self):
        return self[0]

    @x.setter
    def x(self, value):
        self[0] = value

    @property
    def y(self):
        return self[1]

    @y.setter
    def y(self, value):
        self[1] = value

    @property
    def z(self):
        return self[2]

    @z.setter
    def z(self, value):
        self[2] = value
