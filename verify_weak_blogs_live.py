import csv
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import urlparse

import requests

INPUT = Path('below_1000_words_blogs.csv')
OUTPUT = Path('below_1000_words_blogs_live_check.csv')
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
TIMEOUT = (5, 30)
MAX_WORKERS = 8


def load_existing():
    if not OUTPUT.exists():
        return {}
    with OUTPUT.open('r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        return {row['url']: row for row in reader}


def format_blog_url(orig_url, slug):
    parsed = urlparse(orig_url)
    if parsed.scheme not in ('http', 'https'):
        parsed = parsed._replace(scheme='https')
    path = parsed.path or '/'
    if not path.endswith('/'):
        path = path + '/'
    if '/blog/' in path or '/blogs/' in path:
        return f'{parsed.scheme}://{parsed.netloc}{path}'
    if slug:
        return f'{parsed.scheme}://{parsed.netloc}/blog/{slug}/'
    return f'{parsed.scheme}://{parsed.netloc}{path}'


def fetch_url(session, url):
    data = {
        'status': 'ERROR',
        'final_url': '',
    }
    try:
        r = session.get(url, timeout=TIMEOUT, allow_redirects=True, stream=True)
        data['status'] = str(r.status_code)
        data['final_url'] = r.url
        # consume a little to ensure we got a body and the connection isn't leaked
        r.raw.read(1)
        r.close()
    except Exception as exc:
        data['status'] = 'ERROR'
        data['final_url'] = repr(exc)
    return data


def process_row(session, row):
    slug = row.get('slug', '').strip()
    orig_url = row.get('url', '').strip()
    blog_url = format_blog_url(orig_url, slug)
    out = {
        'title': row.get('title', '').strip(),
        'words': row.get('words', '').strip(),
        'date': row.get('date', '').strip(),
        'year': row.get('year', '').strip(),
        'categories': row.get('categories', '').strip(),
        'seo_score': row.get('seo_score', '').strip(),
        'focus_keyword': row.get('focus_keyword', '').strip(),
        'url': orig_url,
        'slug': slug,
        'orig_url': orig_url,
        'blog_url': blog_url,
        'orig_status': '',
        'orig_final_url': '',
        'blog_status': '',
        'blog_final_url': '',
        'checked': 'yes',
    }

    orig_result = fetch_url(session, orig_url)
    blog_result = fetch_url(session, blog_url)
    out['orig_status'] = orig_result['status']
    out['orig_final_url'] = orig_result['final_url']
    out['blog_status'] = blog_result['status']
    out['blog_final_url'] = blog_result['final_url']
    return out


def main():
    existing = load_existing()
    with INPUT.open('r', encoding='utf-8', newline='') as inf:
        reader = csv.DictReader(inf)
        rows = list(reader)

    to_process = [row for row in rows if row['url'] not in existing]
    print('total rows', len(rows), 'already_processed', len(existing), 'remaining', len(to_process), file=sys.stderr)

    fieldnames = [
        'title', 'words', 'date', 'year', 'categories', 'seo_score', 'focus_keyword',
        'url', 'slug', 'orig_url', 'blog_url', 'orig_status', 'orig_final_url',
        'blog_status', 'blog_final_url', 'checked'
    ]

    mode = 'a' if OUTPUT.exists() else 'w'
    with OUTPUT.open(mode, encoding='utf-8', newline='') as outf:
        writer = csv.DictWriter(outf, fieldnames=fieldnames)
        if mode == 'w':
            writer.writeheader()
        session = requests.Session()
        session.headers.update({'User-Agent': USER_AGENT})
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            futures = {executor.submit(process_row, session, row): row for row in to_process}
            completed = 0
            for future in as_completed(futures):
                row = futures[future]
                out = future.result()
                writer.writerow(out)
                completed += 1
                if completed % 25 == 0 or completed == len(to_process):
                    print('appended', completed, 'of', len(to_process), file=sys.stderr)
                    outf.flush()

if __name__ == '__main__':
    main()
