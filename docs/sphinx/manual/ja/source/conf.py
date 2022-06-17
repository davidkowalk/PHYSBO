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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import sys
import os

sys.path.insert(0, os.path.abspath("../../../../../physbo"))

# -- Project information -----------------------------------------------------

project = "PHYSBO"
copyright = "2020-, PHYSBO developers"
author = "PHYSBO developers"

# The short X.Y version.
version = "1.1"
# The full version, including alpha/beta/rc tags.
release = "1.1.0"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "nbsphinx",
]

numfig = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["../../_templates"]

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "ja"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "**.ipynb_checkpoints"]
for t in ("tag-latex", "tag-latexpdf", "tag-latexpdfja"):
    if t in tags:
        exclude_patterns.append("api")

# The suffix of source filenames.
source_suffix = [".rst", ".md"]

from recommonmark.parser import CommonMarkParser

source_parsers = {
    ".md": CommonMarkParser,
}

pygments_style = "sphinx"

nbsphinx_execute = "never"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = "alabaster"
html_theme = "sphinx_rtd_theme"
html_log = "logo.png"
html_theme_options = {"logo_only": True}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["../../_static"]

master_doc = "index"

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_engine = 'uplatex'
# latex_docclass = {"manual": "jsbook"}
latex_logo = "../../_static/logo.png"


# -- configuring _template/version.html -------------------------------------

html_context = {}

html_context["ENABLE_VERSIONING"] = os.environ.get("CI", "false")

html_context["languages"] = [("en"), ("ja")]
html_context["current_lang"] = language

current_version = os.environ.get("TARGET_NAME", "")
if not current_version:
    current_version = release
html_context["current_version"] = current_version

html_context["branches"] = ["develop", "master"]
html_context["tags"] = []
exclude_tags = ["v0.1.0", "v0.2.0", "v0.3.0"]

try:
    import git

    repo = git.Repo(search_parent_directories=True)
    tags = list(map(str, repo.tags))
    tags.sort(reverse=True)
    for tag in tags:
        if tag not in exclude_tags:
            html_context["tags"].append(tag)
except:
    pass

if current_version not in html_context["branches"]:
    if current_version not in html_context["tags"]:
        html_context["branches"].append(current_version)
