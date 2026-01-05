# Configuration file for the Sphinx documentation builder.
import os
import sys
from datetime import datetime

# Add TISCOPE package to path
sys.path.insert(0, os.path.abspath('/data1/ningweixi/HOME/projects/TISCOPE/src'))

# -- Project information -----------------------------------------------------

project = 'TISCOPE'
author = "Yuzhe Li, Weixi Ning"
copyright = f'{datetime.now():%Y}, {author}.'
release = "0.0.1"

# -- General configuration ---------------------------------------------------

nitpicky = True
needs_sphinx = '2.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosummary',
    'sphinx_autodoc_typehints',
    'nbsphinx'
]

# Generate the API documentation when building
autosummary_generate = True
autodoc_member_order = 'bysource'

napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_use_rtype = True
napoleon_use_param = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'

html_theme_options = dict(navigation_depth=4, logo_only=True)
html_context = dict(
    display_github=True,
    github_user='zhangqf-lab',
    github_repo='TISCOPE',
    github_version='master',
    conf_py_path='/docs/source/',
)
html_static_path = ['_static']
html_show_sphinx = False
html_logo = '_static/img/logo_white.png'
