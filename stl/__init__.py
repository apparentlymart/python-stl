
import stl.ascii
import stl.binary


def read_ascii_file(file):
    return stl.ascii.parse(file)


def read_binary_file(file):
    return stl.binary.parse(file)


def read_ascii_string(data):
    from StringIO import StringIO
    return parse_ascii_file(StringIO(data))


def read_binary_string(data):
    from StringIO import StringIO
    return parse_binary_file(StringIO(data))
