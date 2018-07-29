#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'JT Guo'
SITENAME = 'iKnowledgeBase'
SITEURL = 'https://ghxdghxd.github.io'
GITHUB_URL = 'https://github.com/ghxdghxd'
PATH = 'content'
TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = 'zh'

STATIC_PATHS = ["pages", 'theme/images', "documents", 'images']
EXTRA_PATH_METADATA = {
    # about.md生成到output下, 表示about.html的路径
    'pages/about.md': {'path': 'about.html'}
}
PLUGIN_PATHS = ['plugins']
PLUGINS = ['tipue_search', "sitemap", "i18n_subsites", "neighbors"]

THEME = "themes/bootstrap4"
DIRECT_TEMPLATES = ["index", "search",
                    "setting", "archives", "tags", "categories"]
# title, link, font-awesome-id(http://fontawesome.io)
MENUITEMS = [('Home', '.', 'fa-home'),
             ('Archive', 'archives.html', 'fa-archive'),
             ("About", "pages/about.html", "fa-user")]

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.7,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

DISPLAY_CATEGORIES_ON_MENU = True  # 显示分类

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

PAGINATED_DIRECT_TEMPLATES = ['index']  # 分页
DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
