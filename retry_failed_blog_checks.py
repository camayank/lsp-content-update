import csv
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import requests

IN_PATH = Path('below_1000_words_blogs_live_check_clean.csv')
OUT_PATH = Path('below_1000_words_blogs_live_check_retry.csv')
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
TIMEOUT = (5, 60)
MAX_WORKERS = 4

rows = list(csv.DictReader(IN_PATH.open(encoding='utf-8')))
error_rows = [row for row in rows if row['blog_status'] != '200']
print('retrying', len(error_rows), 'failed blog rows')

session = requests.Session()
session.headers.update({'User-Agent': USER_AGENT})


def fetch(url):
    try:
        r = session.get(url, timeout=TIMEOUT, allow_redirects=True, stream=True)
        status = str(r.status_code)
        final = r.url
        r.raw.read(1)
        r.close()
    except Exception as exc:
        status = 'ERROR'
        final = repr(exc)
    return status, final


def retry_row(row):
    status, final = fetch(row['blog_url'])
    row['blog_status'] = status
    row['blog_final_url'] = final
    return row

with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
    futures = {executor.submit(retry_row, row): row for row in error_rows}
    completed = 0
    for future in as_completed(futures):
        completed += 1
        if completed % 10 == 0 or completed == len(error_rows):
            print('completed', completed, 'of', len(error_rows))

with OUT_PATH.open('w', encoding='utf-8', newline='') as outf:
    writer = csv.DictWriter(outf, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

final_rows = list(csv.DictReader(OUT_PATH.open(encoding='utf-8')))
print('final total', len(final_rows))
print('blog 200 count', sum(1 for r in final_rows if r['blog_status'] == '200'))
print('blog error count', sum(1 for r in final_rows if r['blog_status'] != '200'))
