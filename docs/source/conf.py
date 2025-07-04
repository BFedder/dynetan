# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))
# sys.path.insert(0, os.path.abspath('../../src/dynetan/'))

#import dynetan

# -- Project information -----------------------------------------------------

project = 'Dynamical Network Analysis'
copyright = '2023, Marcelo C. R. Melo ; Rafael C. Bernardi'
author = 'Marcelo C. R. Melo ; Rafael C. Bernardi'

# The default replacements for |version| and |release|, also used in various
# other places throughout the built documents.
#
# The short X.Y version.

#version = dynetan.__version__

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['myst_parser', 'sphinx.ext.autodoc', 'sphinx.ext.napoleon',
              'sphinx_rtd_theme']

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

autodoc_typehints = "description"

nitpicky = True
nitpick_ignore = [
    ('py:class', 'MDAnalysis.AtomGroup'),
    ('py:class', 'pandas.DataFrame'),
    ('py:class', 'networkx.Graph'),
    ('py:class', 'numpy.ndarray'),
    ('py:class', 'numpy.typing.NDArray.numpy.int64'),
    ('py:class', 'numpy.typing.NDArray.numpy.float64'),
    ('py:class', 'multiprocessing.context.BaseContext.Queue'),
    ('py:class', 'Queue'),
]


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

#autodoc_default_options = {'imported-members': True}

# This helps speed up the doc compilation time by avoiding the loading
#   of multiple dependency packages.
autodoc_mock_imports = ["numpy","np","MDAnalysis","mda","multiprocessing","mp",
                        "networkx","nx","pandas","pd",
                        "community","colorama", "operator", "collections",
                        "pickle", "h5py","numba",
                        "MDAnalysis.lib.NeighborSearch",
                        "MDAnalysis.coordinates.memory",
                        "MDAnalysis.analysis.base",
                        "MDAnalysis.analysis",
                        "MDAnalysis.analysis.distances"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'

# on_rtd is whether on readthedocs.org, this line of code grabbed from docs.readthedocs.org...
on_rtd = os.environ.get("READTHEDOCS", None) == "True"
if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = "sphinx_rtd_theme"
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
else:
    html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
