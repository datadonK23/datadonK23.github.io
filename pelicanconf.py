#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Thomas Treml'
SITENAME = 'Thomas Treml'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Vienna'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

LOAD_CONTENT_CACHE = False
ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'
TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''
INDEX_SAVE_AS = 'blog_index.html'


THEME = "../pelican-themes/my-pelican-bootstrap3"
BOOTSTRAP_THEME = "flatly"
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['i18n_subsites', 'pelican-ipynb.markup']
MARKUP = ('md', 'ipynb')
#IPYNB_IGNORE_CSS=True
PYGMENTS_STYLE = 'github'
STATIC_PATHS = ['images' , 'notebooks']

#FAVICON = 'images/favicon.png'
DISPLAY_CATEGORIES_ON_MENU = False
CC_LICENSE = "CC-BY"
SIDEBAR_ON_LEFT = True
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (
    ('About Me', '/pages/about.html'),
    ('Work', '/pages/work.html'),
    ('Imprint', '/pages/imprint.html'))
SOCIAL = (('twitter', 'https://twitter.com/datadonk23'),
          ('github', 'https://github.com/donK23'),
          ('linkedin', 'https://www.linkedin.com/in/thomastreml/', 'linkedin'),
          ('medium', 'https://medium.com/@datadonk23', 'medium'),
          ('instagram', 'https://www.instagram.com/datadonk23/', 'instagram'),
          ('facebook', 'https://www.facebook.com/treml.thomas', 'facebook'))
DISABLE_SIDEBAR_TITLE_ICONS = True
ABOUT_ME = "<b>Data Scientist</b><br>&hearts; Donkies &amp; Cycling<br><small>&#9737; Rural AT</small>"
AVATAR = "images/profile.png"
