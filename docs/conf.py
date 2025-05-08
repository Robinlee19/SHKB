# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Senior High Knowledge Base'
copyright = '2025, Robinlee19'
author = 'Robinlee19'
release = 'v1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinxcontrib.katex']

templates_path = ['_templates']
exclude_patterns = []

language = 'zh'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
#html_theme_options['wide_mode'] = True
html_static_path = ['_static']
html_search_language = 'zh'

katex_css_path = 'katex.min.css'
katex_js_path = 'katex.min.js'
katex_autorender_path = 'auto-render.min.js'
katex_inline = [r'$', r'$']
katex_display = [r'\[', r'\]']
katex_prerender = False
katex_options = r'''{
    displayMode: true,
    macros: {
        "\\RR": "\\mathbb{R}",
        "\\i": "\\mathrm{i}",
        "\\e": "\\mathrm{e}^{#1}",
        "\\vec": "\\mathbf{#1}",
        "\\x": "\\vec{x}",
        "\\d": "\\operatorname{d}\\!{}",
        "\\dirac": "\\operatorname{\\delta}\\left(#1\\right)",
        "\\scalarprod": "\\left\\langle#1,#2\\right\\rangle",
    }
}'''