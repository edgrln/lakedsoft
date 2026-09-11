AUTHOR = 'Edgar L'
SITENAME = 'Lakedsoft'
SITEURL = ""
# One-line description used in llms.txt (see bottom of this file) and other
# machine-readable summaries of the site.
SITE_DESCRIPTION = "Практические статьи и разборы по data- и AI-инжинирингу."

# Google Analytics 4 Measurement ID (direct gtag.js, no Tag Manager
# container involved). Empty here (dev) on purpose - set for real in
# publishconf.py only, so `make devserver`/local testing doesn't report
# hits into GA. Read directly as {{ GA_MEASUREMENT_ID }} in base.html/
# landing.html (no JINJA_GLOBALS needed - Pelican exposes all settings to
# templates automatically).
GA_MEASUREMENT_ID = ''

PATH = "content"

THEME = "themes/mytheme"
AUTHORS_INFO = {
    'Edgar L': {
        'avatar': 'https://avatars.githubusercontent.com/u/78014277?v=4',
        'title': 'Технический автор — AI и Data',
        'linkedin': 'https://www.linkedin.com/in/edgarlakshin/',
        'github': 'https://github.com/edgrln',
    },
}

CTA_TITLE = "Построим что-то стоящее"
CTA_TEXT = "Опишите задачу — обсудим её напрямую, без продающих презентаций."
CTA_BUTTON_TEXT = "Написать нам"
CTA_BUTTON_LINK = "mailto:info@lakedsoft.com"
CTA_FOOTNOTE = "info@lakedsoft.com · Удалённо по Европе"

TIMEZONE = 'Europe/Rome'

# Single-language site (Russian) - see UI_STRINGS below. DEFAULT_LANG must
# match every content file's `Lang:` metadata (or its absence, which
# defaults to this): Content.get_url_setting() only falls back to
# {type}_LANG_URL/SAVE_AS when an item's lang differs from this, and this
# site no longer defines those settings (removed together with the FR/DE/ES
# infrastructure - see CLAUDE.md "Multi-language content" history if that
# ever needs reviving).
DEFAULT_LANG = 'ru'

# Single-language site (Russian): UI_STRINGS is a flat dict (not keyed by
# language) for template chrome (nav/footer/buttons/etc.) - NOT for content
# itself (that's just written in Russian directly under content/). Every
# template does `{% set t = UI_STRINGS %}` (see base.html) and reads
# `t.some_key`. This used to be a per-language dict with a LANGUAGES/
# LANGUAGE_NAMES switcher and FR/DE/ES bundles - see CLAUDE.md "Multi-
# language content" for that history if the site needs another language
# again; reviving it means re-adding LANGUAGES/LANGUAGE_NAMES, nesting this
# dict back under language codes, and re-adding ARTICLE_LANG_URL/SAVE_AS +
# PAGE_LANG_URL/SAVE_AS below.
UI_STRINGS = {
    'blog_nav': 'Блог',
    'all_posts': 'Все статьи',
    'latest_posts': 'Последние статьи',
    'read_more': 'Читать дальше',
    'back_to_posts': '← Ко всем статьям',
    'tags': 'Теги:',
    'min_read': 'мин. чтения',
    'loading_more': 'Загружаем ещё статьи…',
    'previous': 'Назад',
    'next': 'Далее',
    'search_placeholder': 'Поиск',
    'no_results': 'Ничего не найдено',
    'see_all_results': 'Показать все результаты',
    'copy_page': 'Скопировать страницу',
    'copy_page_md': 'Скопировать как Markdown',
    'view_as_md': 'Открыть как Markdown',
    'open_in': 'Открыть в {name}',
    'copied': 'Скопировано!',
    'copy_failed': 'Не удалось скопировать',
    'ready_to_start': 'Готовы начать?',
    'cookie_settings': 'Настройки cookie',
    'cookie_policy': 'Политика cookie',
    'category_label': 'Категория:',
    'tag_label': 'Тег:',
    'authors_title': 'Авторы',
    'archives_title': 'Архив',
    'posts_heading': 'Статьи',
    'page_not_found': 'Страница не найдена',
    'go_home': 'На главную',
}

import datetime as _datetime

JINJA_GLOBALS = {
    'UI_STRINGS': UI_STRINGS,
    # Footer copyright year (base.html) - computed once at build time.
    'CURRENT_YEAR': _datetime.date.today().year,
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll. Both "Cookie Policy" and "Cookie settings" used to live here as
# dead "#" links - they're now hardcoded directly in base.html's footer
# instead: "Cookie Policy" links to the real content/pages/cookie-policy.md
# page (needs {{ SITEURL }}, which a plain LINKS entry can't carry per
# dev/prod build), and "Cookie settings" is a data-cc="show-preferencesModal"
# button (needs to trigger JS, not navigate anywhere).
LINKS = []

# Social widget
SOCIAL = [
    ("Git Hub", "https://github.com/edgrln/datacloudhero_v2"),
]

DEFAULT_PAGINATION = 10

# Clean stale files (e.g. old *.html paths) before each build
DELETE_OUTPUT_DIRECTORY = True

# Explicit plugin list. Pelican auto-loads any installed pelican.plugins.*
# package if PLUGINS is left unset, which makes builds depend on whatever
# happens to be pip-installed in a given environment - pin it down instead.
PLUGINS = ['sitemap']
SITEMAP = {
    'format': 'xml',
    'exclude': [
        # A JSON data file for the client-side search widget, not a page.
        r'blog/search-index\.json$',
    ],
    'priorities': {
        'articles': 0.6,
        'indexes': 0.5,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    },
}

# All blog content lives under /blog/ — the site root is a separate static
# landing page (see STATIC_PATHS below), not generated by Pelican.
ARTICLE_URL = 'blog/{slug}/'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'
PAGE_URL = 'blog/{slug}/'
PAGE_SAVE_AS = 'blog/{slug}/index.html'
# This site used to be multi-language (EN default + FR/DE/ES), with
# ARTICLE_LANG_URL/SAVE_AS and PAGE_LANG_URL/SAVE_AS routing non-default-
# language content to a /{lang}/ prefix - see CLAUDE.md "Multi-language
# content" for that history. Every content file is Russian now (DEFAULT_LANG),
# so those settings were removed; re-add both pairs (and LANGUAGES/UI_STRINGS
# nesting - see above) if the site needs another language again.
AUTHOR_URL = 'blog/author/{slug}/'
AUTHOR_SAVE_AS = 'blog/author/{slug}/index.html'
CATEGORY_URL = 'blog/category/{slug}/'
CATEGORY_SAVE_AS = 'blog/category/{slug}/index.html'
TAG_URL = 'blog/tag/{slug}/'
TAG_SAVE_AS = 'blog/tag/{slug}/index.html'

INDEX_SAVE_AS = 'blog/index.html'
TAGS_SAVE_AS = 'blog/tags.html'
TAGS_URL = 'blog/tags.html'
CATEGORIES_SAVE_AS = 'blog/categories.html'
CATEGORIES_URL = 'blog/categories.html'
AUTHORS_SAVE_AS = 'blog/authors.html'
AUTHORS_URL = 'blog/authors.html'
ARCHIVES_SAVE_AS = 'blog/archives.html'
ARCHIVES_URL = 'blog/archives.html'

# Client-side search index (see themes/mytheme/templates/search.html)
DIRECT_TEMPLATES = ["index", "tags", "categories", "authors", "archives", "search"]
SEARCH_SAVE_AS = "blog/search-index.json"
SEARCH_URL = "blog/search-index.json"

# Landing page: content/pages/landing.html is a real Pelican Page (see
# themes/mytheme/templates/landing.html), NOT run through the blog
# theme/templates - it has its own standalone <head>/<body> shell (Tailwind
# CDN, Alpine.js, custom fonts/CSS) unrelated to base.html. Its per-page
# <meta name="save_as"/"url"/"template"> tags route it to output/index.html
# using the "landing" template instead of the blog PAGE_URL/PAGE_SAVE_AS
# pattern below. (It used to be a hand-copied static file; converted so it
# can go through Pelican's normal pipeline - i18n plugins, Jinja variables,
# etc. - like any other content.)
#
# favicon.ico is duplicated to the site root here (same file as
# themes/mytheme/static/img/favicon.ico). Browsers fall back to fetching
# /favicon.ico at the domain root for tabs that have no <link rel="icon">
# to read from - e.g. the raw-text blog/{slug}.md mirrors - so a root-level
# copy is what lets those tabs pick up a favicon at all.
#
# extra/index.md is a short hand-written Markdown summary of the landing
# page (NOT auto-derived from landing.html - that page is a big Alpine.js
# file with no clean text source to extract, e.g. the FAQ copy only exists
# inside an Alpine `x-for` JS array). Keep it in sync by hand when the pitch
# on the landing page changes materially.
STATIC_PATHS = [
    'extra/index.md',
    'extra/favicon.ico',
]
EXTRA_PATH_METADATA = {
    'extra/index.md': {'path': 'index.md'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}
# Keep the article/page generators from also trying to parse content/extra
# (the static passthrough files above) as blog content. ARTICLE_PATHS
# defaults to [""] - i.e. Pelican's ArticlesGenerator walks the *entire*
# content/ tree, including content/pages/ - so 'pages' has to be excluded
# here too, or content/pages/landing.html gets picked up as both an
# Article and a Page and they race to write the same output/index.html.
ARTICLE_EXCLUDES = ['extra', 'pages']
PAGE_EXCLUDES = ['extra']

import json as _json
JINJA_FILTERS = {"tojson": _json.dumps}

# --- Markdown mirrors (Stripe-style /docs/foo.md) --------------------------
# Alongside every rendered blog/{slug}/index.html, write a plain
# blog/{slug}.md containing the article's raw Markdown body. This gives
# LLMs/scrapers/"copy as markdown" buttons a clean source to fetch instead
# of having to parse the HTML page.
import os as _os
import re as _re

# --- og:image / twitter:image support ---------------------------------
# base.html uses this to pick an article's social-share image: the first
# <img> found in its rendered HTML body, falling back to the sitewide
# social-card.png (same one the landing page uses) when an article has no
# image, or on non-article pages (the /blog/ index, tags, categories, ...).
# Without this, unfurlers (Telegram etc.) fell back to scraping whatever
# <img> happens to appear first in the page HTML, which was the author's
# avatar from partials/author_card.html.
_IMG_SRC_RE = _re.compile(r'<img[^>]+src=["\']([^"\']+)["\']')


def _first_image(html, site_url=''):
    """Return the absolute URL of the first <img> in a rendered HTML
    string, or None if there isn't one. A relative src is resolved
    against site_url."""
    if not html:
        return None
    match = _IMG_SRC_RE.search(html)
    if not match:
        return None
    src = match.group(1)
    if src.startswith(('http://', 'https://', 'data:')):
        return src
    if site_url:
        return site_url.rstrip('/') + '/' + src.lstrip('/')
    return src


JINJA_FILTERS['first_image'] = _first_image

_METADATA_LINE_RE = _re.compile(r'^[A-Za-z][\w ]*:\s')


def _strip_pelican_metadata(raw_text):
    """Return the article body, with the leading `Key: value` metadata
    block (Title/Date/Author/...) that Pelican reads off the top of a
    Markdown source file removed."""
    lines = raw_text.splitlines()
    body_start = 0
    for idx, line in enumerate(lines):
        if not line.strip():
            body_start = idx + 1
            break
        if not _METADATA_LINE_RE.match(line):
            # Doesn't look like a metadata block at all - keep everything.
            body_start = 0
            break
    else:
        body_start = len(lines)
    return "\n".join(lines[body_start:]).strip() + "\n"


def _write_markdown_mirrors(article_generator):
    site_url = article_generator.settings.get('SITEURL', '') or ''
    for article in article_generator.articles:
        source_path = getattr(article, 'source_path', None)
        if not source_path or not _os.path.exists(source_path):
            continue

        with open(source_path, encoding='utf-8') as f:
            body = _strip_pelican_metadata(f.read())

        canonical = f"{site_url}/{article.url}" if site_url else f"/{article.url}"
        header = (
            f"# {article.title}\n\n"
            f"> Source: {canonical}\n"
            f"> Published: {article.date:%Y-%m-%d}\n\n"
        )

        # blog/{slug}/index.html -> blog/{slug}.md
        md_relpath = _os.path.dirname(article.save_as) + '.md'
        md_path = _os.path.join(article_generator.output_path, md_relpath)
        _os.makedirs(_os.path.dirname(md_path), exist_ok=True)
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(header + body)


def _collapse_ws(text):
    return _re.sub(r'\s+', ' ', text or '').strip()


def _plain_summary(article):
    """A one-line, tag-free description for an article: prefer the
    `Summary:` metadata, falling back to Pelican's auto-generated summary.
    Pelican's Markdown reader runs both through the Markdown->HTML
    converter, so either way we strip tags before using it."""
    raw = article.metadata.get('summary') or article.summary or ''
    return _collapse_ws(_re.sub(r'<[^>]+>', '', raw))


def _write_llms_txt(article_generator):
    """Write an /llms.txt index (per the llmstxt.org convention) listing
    every article/landing page and its Markdown mirror, so LLM tools can
    discover and fetch the site's content without scraping HTML."""
    settings = article_generator.settings
    site_url = settings.get('SITEURL', '') or ''
    site_name = settings.get('SITENAME', '')
    description = settings.get('SITE_DESCRIPTION', '')

    def url_for(relpath):
        return f"{site_url}/{relpath}" if site_url else f"/{relpath}"

    lines = [
        f"# {site_name}", "", f"> {description}", "",
        "## Site", "",
        f"- [Homepage]({url_for('index.md')}): Services, tech stack, process and contact.",
        "",
        "## Blog", "",
    ]

    articles = sorted(article_generator.articles, key=lambda a: a.date, reverse=True)
    for article in articles:
        md_relpath = _os.path.dirname(article.save_as) + '.md'
        desc = _plain_summary(article)
        entry = f"- [{article.title}]({url_for(md_relpath)})"
        if desc:
            entry += f": {desc}"
        lines.append(entry)
    lines.append("")

    path = _os.path.join(article_generator.output_path, 'llms.txt')
    _os.makedirs(_os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines) + "\n")


def _write_robots_txt(article_generator):
    """Write a minimal, permissive /robots.txt that just points crawlers at
    the sitemap. Note: this domain is proxied through Cloudflare, which has
    been observed overriding/intercepting robots.txt at the edge with its
    own "Content Signals" policy text regardless of what the origin serves
    - if that's still happening, this file won't be what crawlers actually
    see, and the fix is in the Cloudflare dashboard, not here."""
    site_url = article_generator.settings.get('SITEURL', '') or ''
    lines = [
        "User-agent: *",
        "Disallow:",
        "",
        f"Sitemap: {site_url}/sitemap.xml" if site_url else "Sitemap: /sitemap.xml",
    ]
    path = _os.path.join(article_generator.output_path, 'robots.txt')
    _os.makedirs(_os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines) + "\n")


from pelican import signals as _signals
_signals.article_generator_finalized.connect(_write_markdown_mirrors)
_signals.article_generator_finalized.connect(_write_llms_txt)
_signals.article_generator_finalized.connect(_write_robots_txt)
# NOTE: no manual sitemap injection for the homepage anymore - now that
# content/pages/landing.html is a real Pelican Page (see STATIC_PATHS
# comment above), it fires `content_written` on its own like any other
# page, and the sitemap plugin queues it through its normal path.
#
# This site used to also connect _expose_translations_to_context and
# _write_lang_blog_indexes here, to hand-render a /{lang}/blog/ index for
# each non-default language (see blog_index_lang.html, now deleted) - see
# CLAUDE.md "Multi-language content" for that history if the site needs
# another language again.

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
