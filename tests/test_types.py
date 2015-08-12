import unittest
from stl.types import *


class TestTypes(unittest.TestCase):

    def test_facet_geometry(self):
        facet = Facet(
            (1, 0, 0),
            [
                (0, 0, 0),
                (1, 0, 0),
                (0, 1, 0),
            ],
        )
        self.assertEqual(facet.a, 1.0)
        self.assertEqual(facet.b, 1.0)
        self.assertAlmostEqual(facet.c, 1.4142135623730951)

        self.assertAlmostEqual(
            facet.perimeter,
            1.0 + 1.0 + 1.4142135623730951,
        )

        self.assertAlmostEqual(facet.area, 0.5)

    def test_solid_geometry(self):
        solid = Solid(
            "test",
            [
                Facet(
                    (1, 0, 0),
                    [
                        (0, 0, 0),
                        (1, 0, 0),
                        (0, 1, 0),
                    ],
                ),
                Facet(
                    (1, 0, 0),
                    [
                        (0, 0, 0),
                        (1, 0, 0),
                        (0, 0, 1),
                    ],
                ),
            ],
        )

        self.assertAlmostEqual(solid.surface_area, 0.5 + 0.5)
