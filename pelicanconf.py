#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Benoit KUGLER'
SITENAME = 'Benoit KUGLER - Page personnelle'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

THEME = "themes/blue-penguin"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)


STATIC_PATHS = ("pdfs", "images",
                )

CACHE_CONTENT = True

DISPLAY_FOOTER = False

OUTPUT_PATH = "docs/"

DISPLAY_HOME = False
DEFAULT_PAGINATION = False
INDEX_SAVE_AS = "enseignement.html"
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = [('Accueil', '/'), ('Publications', '/publications.html'), ('Enseignement', '/enseignement.html') ]
