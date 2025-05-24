# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
from pathlib import Path
import django

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
os.environ['DJANGO_SETTINGS_MODULE'] = 'memcollection.settings.dev'
django.setup()

project = 'MEMCollection-Wagtail'
copyright = '2025, Megan McCarty'
author = 'Megan McCarty'
release = '0.4.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx_wagtail_theme'
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_wagtail_theme'
html_theme_options = dict(
    project_name = "MEMCollection-Wagtail",
    logo = "img/logo-white.png",
    logo_alt = "MEMCollection-Wagtail",
    logo_height = 59,
    logo_url = "/",
    logo_width = 45,
    github_url = "https://github.com/Meganmccarty/memcollection-wagtail/blob/main/docs/",
    header_links = '',
    footer_links = '',
)
html_last_updated_fmt = "%b %d, %Y."
html_static_path = ['_static']
