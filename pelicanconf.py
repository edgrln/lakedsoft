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
CTA_BUTTON_LINK = "mailto:info@lakedapp.com"
CTA_FOOTNOTE = "info@lakedapp.com · Удалённо по Европе"

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
#
# extra/CNAME copies to output/CNAME so GitHub Pages' custom domain
# (lakedapp.com) survives every Actions-based deploy - without a CNAME file
# physically in the published artifact, GitHub can silently drop the custom
# domain setting on redeploy. Must stay in sync with SITEURL in
# publishconf.py and the custom domain configured in the repo's Pages
# settings.
STATIC_PATHS = [
    'extra/index.md',
    'extra/favicon.ico',
    'extra/CNAME',
]
EXTRA_PATH_METADATA = {
    'extra/index.md': {'path': 'index.md'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'},
}
# Article source files live under content/blog/ (not flat in content/ -
# that grew cluttered as soon as an article needed colocated assets, e.g.
# content/blog/2026-09-14-agent-memory-framework/ below bundles a post with
# its diagram SVGs so {attach} can find them - the folder name is
# {date}-{slug}, not just the date, so same-day articles never collide).
# ARTICLE_PATHS defaults to [""], meaning
# Pelican's ArticlesGenerator otherwise walks the *entire* content/ tree,
# including content/pages/ and content/extra/ - scoping it to 'blog' here
# means those never need excluding: without this, content/pages/landing.html
# would get picked up as both an Article and a Page and they'd race to
# write the same output/index.html.
ARTICLE_PATHS = ['blog']
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
from html.parser import HTMLParser as _HTMLParser
from pelican.generators import ArticlesGenerator as _ArticlesGenerator
from pelican.generators import PagesGenerator as _PagesGenerator

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


# --- Markdown mirrors for standalone landing pages -------------------------
# Same idea as _write_markdown_mirrors above, but for the raw-HTML `Page`
# family documented in CLAUDE.md ("A second standalone landing page:
# /data-ai/") - those pages have no clean Markdown source to copy (they're
# hand-authored HTML: header/nav, hero, cards, contact-form modal, footer),
# so the mirror has to be built by parsing the rendered markup and keeping
# only the "pitch" - headings, paragraphs, service-card/FAQ text - while
# dropping chrome that would otherwise leak in as noise: the header/footer
# (nav links duplicated 2-3x), the contact-form modal (field labels, the
# honeypot input, the Turnstile widget, the submit button's spinner text),
# CTA buttons ("Написать нам →" reads as a floating non-sequitur outside
# its button), SVG icons (no text anyway), and the quiet
# .lk-hero-secondary cross-link line (chrome, not pitch).
#
# _LANDING_MIRROR_TEMPLATES is the opt-in list: only pages whose
# `template` metadata is a key here get a mirror written - the value is
# a short one-line description used for that page's entry in
# llms.txt's "## Site" section (Page objects have no Summary: metadata
# convention the way articles do, so there's nothing to derive one
# from automatically). The root landing page ('landing') is
# deliberately excluded - its Markdown representation is
# content/extra/index.md (hand-written, copied to output/index.md via
# STATIC_PATHS; see pelicanconf.py's STATIC_PATHS comment) - the
# dirname(save_as)+'.md' scheme below would collide with that file for
# a page saved at the site root (dirname('index.html') is '', giving a
# nonsensical '.md' path), so root is out of scope here by design, not
# oversight. Add a new template name here when another standalone
# landing page (beyond /data-ai/) should get an auto mirror and an
# llms.txt entry.
_LANDING_MIRROR_TEMPLATES = {
    'data-ai': 'B2B pitch: data pipelines, BI, and AI solutions on Google Cloud.',
}

_MAIN_RE = _re.compile(r'<main\b[^>]*>(.*)</main>', _re.DOTALL)
_SVG_RE = _re.compile(r'<svg\b.*?</svg>', _re.DOTALL)
_BUTTON_RE = _re.compile(r'<button\b.*?</button>', _re.DOTALL)
_BTN_LINK_RE = _re.compile(r'<a\b[^>]*\bclass="[^"]*\bbtn\b[^"]*"[^>]*>.*?</a>', _re.DOTALL)
_HERO_SECONDARY_RE = _re.compile(r'<p\b[^>]*\bclass="lk-hero-secondary"[^>]*>.*?</p>', _re.DOTALL)
_HONEYPOT_RE = _re.compile(r'<input\b[^>]*\bclass="lk-honeypot"[^>]*/?>')


def _strip_balanced_div(html, needle):
    """Remove the first <div ...>...</div> block whose opening tag
    contains `needle` (e.g. a class name), correctly skipping over <div>
    tags nested inside it rather than stopping at the first </div> -
    which is what makes this safe for the contact-form modal
    (.dialog-backdrop wraps a nested .dialog, which itself wraps several
    .field divs) where a plain non-greedy regex would truncate the match
    at the first inner </div> and leave the rest of the form dangling in
    the output. Returns `html` unchanged if `needle` isn't found, or if
    the markup turns out not to balance (safer to leave content in than
    to risk mangling the page)."""
    start = html.find(needle)
    if start == -1:
        return html
    open_tag_start = html.rfind('<div', 0, start)
    if open_tag_start == -1:
        return html
    pos = html.index('>', start) + 1
    depth = 1
    while depth > 0:
        next_open = html.find('<div', pos)
        next_close = html.find('</div>', pos)
        if next_close == -1:
            return html
        if next_open != -1 and next_open < next_close:
            depth += 1
            pos = next_open + len('<div')
        else:
            depth -= 1
            pos = next_close + len('</div>')
    return html[:open_tag_start] + html[pos:]


class _MainContentToMarkdown(_HTMLParser):
    """Turns the pre-cleaned inner HTML of a landing page's <main> into
    plain Markdown. Only a handful of tags/classes get special treatment
    - h1-h4 become '#'..'####' headings, <div class="card-title"> is
    promoted to a level-4 heading too (it's a service card's title, but
    isn't a real heading tag), <summary> (an FAQ question) and
    <div class="lk-stack-label"> (a stack category like "Хранение") are
    bolded, <div class="lk-kicker"/"lk-step-num"> (a section's small
    overline, or a process step's "01") are italicized so they read as
    a label rather than a stray sentence in front of the heading/step
    that follows, and <span class="tag ..."> pills are comma-joined
    into one line. Everything else's text just flows through as a
    plain paragraph in document order - deliberately not trying to
    reconstruct bullet lists/tables for every card/step/stat shape,
    since the caller has already stripped the actual noise (see the
    regexes and _strip_balanced_div above) and a plain paragraph per
    block reads fine for an LLM/search-index consumer even without
    perfect nesting."""

    _HEADING_LEVEL = {'h1': 1, 'h2': 2, 'h3': 3, 'h4': 4}
    _BLOCK_TAGS = {'div', 'section', 'p', 'details', 'li', 'ul', 'ol'}
    _EM_CLASSES = {'lk-kicker', 'lk-step-num'}
    _STRONG_CLASSES = {'lk-stack-label'}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.blocks = []
        self._buf = []
        self._heading_level = None
        self._style = None  # None | 'strong' | 'em'

    @staticmethod
    def _classes(attrs):
        for name, value in attrs:
            if name == 'class':
                return (value or '').split()
        return []

    def _flush(self):
        text = _collapse_ws(''.join(self._buf))
        # Whitespace text nodes between adjacent tag pills (e.g.
        # "<span>A</span>\n  <span>B</span>") land in the buffer before
        # the ", " separator inserted in handle_starttag, so collapsing
        # runs of whitespace above still leaves "A , B" - tidy that up.
        text = _re.sub(r'\s+,', ',', text)
        self._buf = []
        if not text:
            return
        if self._heading_level:
            self.blocks.append('#' * self._heading_level + ' ' + text)
        elif self._style == 'strong':
            self.blocks.append('**' + text + '**')
        elif self._style == 'em':
            self.blocks.append('*' + text + '*')
        else:
            self.blocks.append(text)

    def handle_starttag(self, tag, attrs):
        classes = self._classes(attrs) if tag == 'div' else ()
        if tag in self._HEADING_LEVEL:
            self._flush()
            self._heading_level = self._HEADING_LEVEL[tag]
        elif tag == 'div' and 'card-title' in classes:
            self._flush()
            self._heading_level = 4
        elif tag == 'div' and self._EM_CLASSES.intersection(classes):
            self._flush()
            self._style = 'em'
        elif tag == 'div' and self._STRONG_CLASSES.intersection(classes):
            self._flush()
            self._style = 'strong'
        elif tag == 'summary':
            self._flush()
            self._style = 'strong'
        elif tag == 'span' and self._buf and _collapse_ws(''.join(self._buf)):
            # A tag pill after an earlier one in the same group - join
            # with a comma instead of letting them run together.
            self._buf.append(', ')
        elif tag in self._BLOCK_TAGS:
            self._flush()

    def handle_endtag(self, tag):
        if tag in self._HEADING_LEVEL or (tag == 'div' and self._heading_level == 4):
            self._flush()
            self._heading_level = None
        elif tag == 'summary' or (tag == 'div' and self._style):
            self._flush()
            self._style = None
        elif tag in self._BLOCK_TAGS:
            self._flush()

    def handle_data(self, data):
        self._buf.append(data)

    def close(self):
        super().close()
        self._flush()


def _page_body_to_markdown(rendered_html):
    """Extract just the <main> content of a rendered landing page and
    convert it to plain Markdown, dropping the chrome described above.
    Returns '' if the page has no <main> (shouldn't happen for a page
    using this family's document shell - see CLAUDE.md)."""
    match = _MAIN_RE.search(rendered_html)
    if not match:
        return ''
    main_html = match.group(1)
    main_html = _strip_balanced_div(main_html, 'class="dialog-backdrop"')
    main_html = _SVG_RE.sub('', main_html)
    main_html = _BUTTON_RE.sub('', main_html)
    main_html = _BTN_LINK_RE.sub('', main_html)
    main_html = _HERO_SECONDARY_RE.sub('', main_html)
    main_html = _HONEYPOT_RE.sub('', main_html)

    parser = _MainContentToMarkdown()
    parser.feed(main_html)
    parser.close()
    return '\n\n'.join(parser.blocks) + '\n'


def _write_page_markdown_mirrors(page_generator, writer=None):
    # Connected to page_writer_finalized (not page_generator_finalized,
    # which fires from generate_context() *before* generate_output() has
    # written anything) because this reads each page's already-rendered
    # output/{page.save_as} HTML off disk - see CLAUDE.md's markdown-
    # mirrors section for why (the raw content file has no clean
    # Markdown to copy the way an article's source .md does; the
    # rendered HTML is what actually has the header/footer/contact-modal
    # chrome removed by page_body_to_markdown, so it has to run after
    # the real write, not before it).
    site_url = page_generator.settings.get('SITEURL', '') or ''
    for page in page_generator.pages:
        if page.metadata.get('template') not in _LANDING_MIRROR_TEMPLATES:
            continue

        out_path = _os.path.join(page_generator.output_path, page.save_as)
        if not _os.path.exists(out_path):
            continue
        with open(out_path, encoding='utf-8') as f:
            rendered_html = f.read()

        body = _page_body_to_markdown(rendered_html)
        canonical = f"{site_url}/{page.url}" if site_url else f"/{page.url}"
        header = f"# {page.title}\n\n> Source: {canonical}\n\n"

        # data-ai/index.html -> data-ai.md
        md_relpath = _os.path.dirname(page.save_as) + '.md'
        md_path = _os.path.join(page_generator.output_path, md_relpath)
        _os.makedirs(_os.path.dirname(md_path) or '.', exist_ok=True)
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


def _write_llms_txt(generators):
    """Write an /llms.txt index (per the llmstxt.org convention) listing
    every standalone landing page and article, plus their Markdown
    mirrors, so LLM tools can discover and fetch the site's content
    without scraping HTML.

    Connected to all_generators_finalized rather than
    article_generator_finalized: this needs both
    ArticlesGenerator.articles and PagesGenerator.pages (to list
    /data-ai/ etc. alongside the blog), and the two generators'
    generate_context() calls aren't guaranteed to run in a particular
    order relative to each other, so article_generator_finalized alone
    can't promise PagesGenerator.pages is populated yet.
    all_generators_finalized fires once every generator's context phase
    has completed - still before any HTML is written, which is fine
    here since only save_as/url/title metadata is needed, not rendered
    content (this used to be article-only, so a page like /data-ai/
    never showed up here at all - only /index.md via the hardcoded
    Homepage line below)."""
    article_generator = next(g for g in generators if isinstance(g, _ArticlesGenerator))
    page_generator = next(g for g in generators if isinstance(g, _PagesGenerator))

    settings = article_generator.settings
    site_url = settings.get('SITEURL', '') or ''
    site_name = settings.get('SITENAME', '')
    description = settings.get('SITE_DESCRIPTION', '')

    def url_for(relpath):
        return f"{site_url}/{relpath}" if site_url else f"/{relpath}"

    lines = [
        f"# {site_name}", "", f"> {description}", "",
        "## Site", "",
        f"- [Homepage]({url_for('index.md')}): AI assistants, Telegram ecosystems, and digital-presence architecture for online experts and small businesses.",
    ]
    for page in page_generator.pages:
        page_desc = _LANDING_MIRROR_TEMPLATES.get(page.metadata.get('template'))
        if page_desc is None:
            continue
        md_relpath = _os.path.dirname(page.save_as) + '.md'
        lines.append(f"- [{page.title}]({url_for(md_relpath)}): {page_desc}")
    lines.append("")
    lines.append("## Blog")
    lines.append("")

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
_signals.all_generators_finalized.connect(_write_llms_txt)
_signals.article_generator_finalized.connect(_write_robots_txt)
_signals.page_writer_finalized.connect(_write_page_markdown_mirrors)
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
