# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
#
# TEMPORARY: lakedsoft.com's DNS/CNAME is not set up yet, so the site is
# actually being served from GitHub Pages' default project-page URL
# (https://edgrln.github.io/lakedsoft/), not the custom domain. SITEURL has
# to match wherever the site is really served from, because templates build
# every CSS/JS/asset link and canonical/OG URL from it
# (e.g. `{{ SITEURL }}/theme/css/classical.css` in landing.html/base.html) —
# pointing it at lakedsoft.com while actually deploying to github.io means
# every stylesheet/script 404s against a domain nothing is served from,
# which is exactly what broke the first deploy (unstyled page, no CSS/JS/
# icons loading). Once lakedsoft.com's DNS is pointed at this GitHub Pages
# deployment (and a CNAME file is added), switch this back to
# "https://lakedsoft.com".
SITEURL = "https://edgrln.github.io/lakedsoft"
RELATIVE_URLS = False

GTM_ID = 'GTM-P6YFW7BQZR'

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""
