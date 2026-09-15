# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
#
# SITEURL must match wherever the site is really served from, because
# templates build every CSS/JS/asset link and canonical/OG URL from it
# (e.g. `{{ SITEURL }}/theme/css/classical.css` in landing.html/base.html).
# The custom domain lakedapp.com is now configured in GitHub Pages settings
# and its DNS points at this deployment (see CNAME below) — pointing
# SITEURL anywhere else (e.g. the old edgrln.github.io/lakedsoft project
# URL) breaks every stylesheet/script link, which is exactly what happened
# during the domain migration (unstyled page, no CSS/JS/icons loading,
# caused by the old project URL 301-redirecting asset requests to
# lakedapp.com over plain http, which browsers block as mixed content on
# an https page).
SITEURL = "https://lakedapp.com"
RELATIVE_URLS = False

GA_MEASUREMENT_ID = 'G-ERML6E6JW9'

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""
