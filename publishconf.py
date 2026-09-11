# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
# NOTE: this assumes lakedsoft.com's DNS/CNAME is pointed at this site's
# deployment. Until that's done, canonical URLs/sitemap/OG tags generated
# by a production build will point at a domain that isn't actually live yet.
SITEURL = "https://lakedsoft.com"
RELATIVE_URLS = False

GTM_ID = 'GTM-ERML6E6JW9'

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""
