import unittest
import pep8
import os.path


tests_dir = os.path.dirname(__file__)
modules_dir = os.path.abspath(os.path.join(tests_dir, "..", "stl"))


class TestCodeStyle(unittest.TestCase):

    def test_pep8_conformance(self):
        pep8style = pep8.StyleGuide()
        result = pep8style.check_files([tests_dir, modules_dir])
        self.assertEqual(
            result.total_errors,
            0,
            "Found pep8 conformance issues",
        )
