Writing STL Files
=================

In order to write an STL file you must first construct a valid
:py:class:`stl.Solid` object containing the data that is to be written.

Files can then be written using :py:meth:`stl.Solid.write_ascii` and
:py:meth:`stl.Solid.write_binary` respectively.
