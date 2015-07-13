
from StringIO import StringIO
import unittest
from stl.ascii import *


class TestScanner(unittest.TestCase):

    def _scanner_for_str(self, string):
        return Scanner(StringIO(string))

    def _get_tokens(self, string):
        scanner = self._scanner_for_str(string)
        tokens = []

        while True:
            token = scanner.get_token()
            if token is not None:
                tokens.append(token)
            else:
                break

        return tokens

    def test_numbers(self):
        tokens = self._get_tokens("1 0.1 -0.1 1e2\n1.2e2 1.2e-2 1.2e+2 1.2E+2")
        self.assertEqual(
            tokens,
            [
                1, 0.1, -0.1, 100, 120, 0.012, 120.0, 120.0,
            ],
        )

        self.assertEqual(
            [tokens[1].start_row, tokens[1].start_col],
            [1, 3],
        )
        self.assertEqual(
            [tokens[5].start_row, tokens[5].start_col],
            [2, 7],
        )

        with self.assertRaises(SyntaxError):
            self._get_tokens("1e1e1")

        with self.assertRaises(SyntaxError):
            self._get_tokens("1.1.1")

        with self.assertRaises(SyntaxError):
            self._get_tokens("--2")

    def test_keywords(self):
        tokens = self._get_tokens("hello world a\nb c _d e_f g2")
        self.assertEqual(
            tokens,
            [
                'hello', 'world', 'a', 'b', 'c', '_d', 'e_f', 'g2',
            ],
        )

        self.assertEqual(
            [tokens[1].start_row, tokens[1].start_col],
            [1, 7],
        )
        self.assertEqual(
            [tokens[4].start_row, tokens[4].start_col],
            [2, 3],
        )

    def test_spaces(self):
        tokens = self._get_tokens(" \n\t")
        self.assertEqual(
            tokens,
            [],
        )

    def test_require_token(self):
        scanner = self._scanner_for_str("baz")
        try:
            scanner.require_token(KeywordToken)
        except SyntaxError:
            self.fail('Unexpected SyntaxError')

        scanner = self._scanner_for_str("baz")
        try:
            scanner.require_token(KeywordToken, "baz")
        except SyntaxError:
            self.fail('Unexpected SyntaxError')

        scanner = self._scanner_for_str("baz")
        with self.assertRaises(SyntaxError):
            scanner.require_token(NumberToken)

        scanner = self._scanner_for_str("baz")
        with self.assertRaises(SyntaxError):
            scanner.require_token(KeywordToken, "foo")


class TestParser(unittest.TestCase):

    def _parse_str(self, string):
        return parse(StringIO(string))

    def test_empty(self):
        with self.assertRaises(SyntaxError):
            self._parse_str('')

    def test_no_facets(self):
        self.assertEqual(
            self._parse_str("solid Baz\nendsolid Baz\n"),
            Solid(name="Baz"),
        )

    def test_inconsistent_name(self):
        with self.assertRaises(SyntaxError):
            self._parse_str("solid Baz\nendsolid Bonk\n")

    def test_facets(self):
        self.assertEqual(
            self._parse_str(
                "solid Baz\n"
                "  facet normal 1 2 3\n"
                "    outer loop\n"
                "      vertex 4 5 6\n"
                "      vertex 7 8 9\n"
                "      vertex 10 11 12\n"
                "    endloop\n"
                "  endfacet\n"
                "  facet normal 1.1 2.1 3.1\n"
                "    outer loop\n"
                "      vertex 4.1 5.1 6.1\n"
                "      vertex 7.1 8.1 9.1\n"
                "      vertex 10.1 11.1 12.1\n"
                "    endloop\n"
                "  endfacet\n"
                "endsolid Baz\n"
            ),
            Solid(
                name="Baz",
                facets=[
                    Facet(
                        normal=Vector3d(1.0, 2.0, 3.0),
                        vertices=(
                            Vector3d(4.0, 5.0, 6.0),
                            Vector3d(7.0, 8.0, 9.0),
                            Vector3d(10.0, 11.0, 12.0),
                        ),
                    ),
                    Facet(
                        normal=Vector3d(1.1, 2.1, 3.1),
                        vertices=(
                            Vector3d(4.1, 5.1, 6.1),
                            Vector3d(7.1, 8.1, 9.1),
                            Vector3d(10.1, 11.1, 12.1),
                        ),
                    ),
                ],
            ),
        )


class TestWriter(unittest.TestCase):

    def assertResultEqual(self, solid, expected):
        f = StringIO('')
        solid.write_ascii(f)
        self.assertEqual(
            f.getvalue(),
            expected,
        )

    def test_empty(self):
        self.assertResultEqual(
            Solid(),
            'solid unnamed\n'
            'endsolid unnamed\n'
        )

    def test_with_facets(self):
        self.assertResultEqual(
            Solid(
                name='withfacets',
                facets=[
                    Facet(
                        normal=(1, 2, 3),
                        vertices=[
                            (4, 5, 6),
                            (7, 8, 9),
                            (10, 11, 12),
                        ],
                    ),
                    Facet(
                        normal=(1.1, 2.1, 3.1),
                        vertices=[
                            (4.1, 5.1, 6.1),
                            (7.1, 8.1, 9.1),
                            (10.1, 11.1, 12.1),
                        ],
                    ),
                ],
            ),
            'solid withfacets\n'
            '  facet normal 1 2 3\n'
            '    outer loop\n'
            '      vertex 4 5 6\n'
            '      vertex 7 8 9\n'
            '      vertex 10 11 12\n'
            '    endloop\n'
            '  endfacet\n'
            '  facet normal 1.1 2.1 3.1\n'
            '    outer loop\n'
            '      vertex 4.1 5.1 6.1\n'
            '      vertex 7.1 8.1 9.1\n'
            '      vertex 10.1 11.1 12.1\n'
            '    endloop\n'
            '  endfacet\n'
            'endsolid withfacets\n'
        )
