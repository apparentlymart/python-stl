
from StringIO import StringIO
import unittest
from stl.binary import *

EMPTY_HEADER = '\0' * 80
T_HDR = '\x73\x6f\x6c\x69\x64\x20\x54\x65\x73\x74\x66\x69\x6c\x65' + ('\0'*66)


class TestParser(unittest.TestCase):

    def _parse_str(self, string):
        return parse(StringIO(string))

    def test_empty(self):
        with self.assertRaises(FormatError):
            self._parse_str('')

    def test_no_facets(self):
        solid = self._parse_str(
            T_HDR + '\0\0\0\0'
        )
        self.assertEqual(
            solid,
            Solid(
                name='Testfile',
                facets=[],
            ),
        )

    def test_missing_facets(self):
        with self.assertRaises(FormatError):
            # Declared that we have two facets but we
            # actually have none.
            self._parse_str(
                T_HDR + '\x02\x00\x00\x00'
            )

    def test_valid(self):
        solid = self._parse_str(
            T_HDR +
            '\x02\x00\x00\x00'  # two facets
            # first facet
            '\x00\x00\x80\x3f'  # normal x = 1.0
            '\x00\x00\x00\x40'  # normal y = 2.0
            '\x00\x00\x40\x40'  # normal z = 3.0
            '\x00\x00\x80\x40'  # vertex x = 4.0
            '\x00\x00\xa0\x40'  # vertex y = 5.0
            '\x00\x00\xc0\x40'  # vertex z = 6.0
            '\x00\x00\xe0\x40'  # vertex x = 7.0
            '\x00\x00\x00\x41'  # vertex y = 8.0
            '\x00\x00\x10\x41'  # vertex z = 9.0
            '\x00\x00\x20\x41'  # vertex x = 10.0
            '\x00\x00\x30\x41'  # vertex y = 11.0
            '\x00\x00\x40\x41'  # vertex z = 12.0
            '\x04\x00'          # four attribute bytes
            '\x00\x00\x80\x7f'  # dummy attribute bytes (float Infinity)
            # second facet
            '\x00\x00\x80\x3f'  # normal x = 1.0
            '\x00\x00\x80\x3f'  # normal y = 1.0
            '\x00\x00\x80\x3f'  # normal z = 1.0
            '\x00\x00\x80\x3f'  # vertex x = 1.0
            '\x00\x00\x80\x3f'  # vertex y = 1.0
            '\x00\x00\x80\x3f'  # vertex z = 1.0
            '\x00\x00\x80\x3f'  # vertex x = 1.0
            '\x00\x00\x80\x3f'  # vertex y = 1.0
            '\x00\x00\x80\x3f'  # vertex z = 1.0
            '\x00\x00\x80\x3f'  # vertex x = 1.0
            '\x00\x00\x80\x3f'  # vertex y = 1.0
            '\x00\x00\x80\x3f'  # vertex z = 1.0
            '\x00\x00'          # no attribute bytes
        )
        self.assertEqual(
            solid,
            Solid(
                name='Testfile',
                facets=[
                    Facet(
                        normal=Vector3d(1.0, 2.0, 3.0),
                        vertices=(
                            Vector3d(4.0, 5.0, 6.0),
                            Vector3d(7.0, 8.0, 9.0),
                            Vector3d(10.0, 11.0, 12.0),
                        ),
                        attributes='\x00\x00\x80\x7f',
                    ),
                    Facet(
                        normal=Vector3d(1.0, 1.0, 1.0),
                        vertices=(
                            Vector3d(1.0, 1.0, 1.0),
                            Vector3d(1.0, 1.0, 1.0),
                            Vector3d(1.0, 1.0, 1.0),
                        ),
                        attributes=None,
                    ),
                ],
            ),
        )


class TestWriter(unittest.TestCase):

    def assertResultEqual(self, solid, expected):
        f = StringIO('')
        solid.write_binary(f)
        self.assertEqual(
            f.getvalue(),
            expected,
        )

    def test_empty(self):
        self.assertResultEqual(
            Solid(),
            EMPTY_HEADER +
            '\0\0\0\0'
        )

    def test_with_facets(self):
        self.assertResultEqual(
            Solid(
                name=None,
                facets=[
                    Facet(
                        normal=Vector3d(1.0, 2.0, 3.0),
                        vertices=(
                            Vector3d(4.0, 5.0, 6.0),
                            Vector3d(7.0, 8.0, 9.0),
                            Vector3d(10.0, 11.0, 12.0),
                        ),
                        attributes=None,
                    ),
                    Facet(
                        normal=Vector3d(1.0, 1.0, 1.0),
                        vertices=(
                            Vector3d(1.0, 1.0, 1.0),
                            Vector3d(1.0, 1.0, 1.0),
                            Vector3d(1.0, 1.0, 1.0),
                        ),
                        attributes=None,
                    ),
                ],
            ),
            EMPTY_HEADER +
            '\x02\x00\x00\x00'  # two facets
            # first facet
            '\x00\x00\x80\x3f'  # normal x = 1.0
            '\x00\x00\x00\x40'  # normal y = 2.0
            '\x00\x00\x40\x40'  # normal z = 3.0
            '\x00\x00\x80\x40'  # vertex x = 4.0
            '\x00\x00\xa0\x40'  # vertex y = 5.0
            '\x00\x00\xc0\x40'  # vertex z = 6.0
            '\x00\x00\xe0\x40'  # vertex x = 7.0
            '\x00\x00\x00\x41'  # vertex y = 8.0
            '\x00\x00\x10\x41'  # vertex z = 9.0
            '\x00\x00\x20\x41'  # vertex x = 10.0
            '\x00\x00\x30\x41'  # vertex y = 11.0
            '\x00\x00\x40\x41'  # vertex z = 12.0
            '\x00\x00'          # no attribute bytes
            # second facet
            '\x00\x00\x80\x3f'  # normal x = 1.0
            '\x00\x00\x80\x3f'  # normal y = 1.0
            '\x00\x00\x80\x3f'  # normal z = 1.0
            '\x00\x00\x80\x3f'  # vertex x = 1.0
            '\x00\x00\x80\x3f'  # vertex y = 1.0
            '\x00\x00\x80\x3f'  # vertex z = 1.0
            '\x00\x00\x80\x3f'  # vertex x = 1.0
            '\x00\x00\x80\x3f'  # vertex y = 1.0
            '\x00\x00\x80\x3f'  # vertex z = 1.0
            '\x00\x00\x80\x3f'  # vertex x = 1.0
            '\x00\x00\x80\x3f'  # vertex y = 1.0
            '\x00\x00\x80\x3f'  # vertex z = 1.0
            '\x00\x00'          # no attribute bytes
        )
