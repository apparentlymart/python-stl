
import stl.ascii
import stl.binary


def parse_ascii_file(file):
    return stl.ascii.parse(file)


def parse_binary_file(file):
    return stl.binary.parse(file)


def parse_ascii_string(data):
    from StringIO import StringIO
    return parse_ascii_file(StringIO(data))


def parse_binary_string(data):
    from StringIO import StringIO
    return parse_binary_file(StringIO(data))
