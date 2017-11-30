# -*- coding: utf-8 -*-

from nbsite.shared_conf import *

project = u'xarray_filters'
authors = u'xarray_filters contributors'
copyright = u'2017 ' + authors
description = 'Short description for html meta description.'

import xarray_filters
version = release = xarray_filters.__version__

html_static_path += ['_static']
html_theme = 'sphinx_ioam_theme'
# logo file etc should be in html_static_path, e.g. _static
html_theme_options = {
#    'custom_css':'bettercolors.css',
#    'logo':'amazinglogo.png',
#    'favicon':'amazingfavicon.ico'
}

# TODO
nbbuild_ipython_startup = ""

_NAV =  (
    ('User Guide', 'user_guide/index'),
    ('FAQ', 'FAQ'),
    ('About', 'about')
)

html_context.update({
    'PROJECT': project,
    'DESCRIPTION': description,
    'AUTHOR': authors,
    # will work without this - for canonical (so can ignore when building locally or test deploying)    
    'WEBSITE_SERVER': 'https://ceball.github.io/xarray_filters',
    'VERSION': version,
    'NAV': _NAV,
    # by default, footer links are same as those in header
    'LINKS': _NAV,
    'SOCIAL': (
        ('Github', '//github.com/ContinuumIO/xarray_filters'),
    )
})
