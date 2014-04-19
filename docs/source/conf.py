
import sys
import os
import pkg_resources

# See what version of tiedye is installed to auto-detect our version.
# In a dev environment this requires that the repo be "installed" using
#   e.g. pip install -e .
detected_version = pkg_resources.get_distribution("stl").version

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'Python STL'
copyright = u'2014, Martin Atkins'
version = detected_version
release = detected_version

exclude_patterns = []

pygments_style = 'sphinx'
html_theme = 'default'
html_static_path = ['_static']

intersphinx_mapping = {
    'http://docs.python.org/': None,
}
