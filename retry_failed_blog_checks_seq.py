import csv
import time
from pathlib import Path
import requests

IN_PATH = Path('below_1000_words_blogs_live_check_clean.csv')
OUT_PATH = Path('below_1000_words_blogs_live_check_retry_seq.csv')
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
TIMEOUT = (5, 60)

rows = list(csv.DictReader(IN_PATH.open(encoding='utf-8')))

# keep all rows and update failures sequentially
session = requests.Session()
session.headers.update({'User-Agent': USER_AGENT})

failed_indices = [i for i, row in enumerate(rows) if row['blog_status'] != '200']
print('retrying', len(failed_indices), 'failed blog URLs')


def check_url(url):
    try:
        r = session.head(url, allow_redirects=True, timeout=TIMEOUT)
        return str(r.status_code), r.url
    except requests.RequestException:
        try:
            r = session.get(url, allow_redirects=True, timeout=TIMEOUT, stream=True)
            final = r.url
            status = str(r.status_code)
            r.raw.read(1)
            r.close()
            return status, final
        except requests.RequestException as exc:
            return 'ERROR', repr(exc)

for count, idx in enumerate(failed_indices, 1):
    row = rows[idx]
    blog_url = row['blog_url']
    status, final = check_url(blog_url)
    row['blog_status'] = status
    row['blog_final_url'] = final
    print(f'{count}/{len(failed_indices)}', blog_url, status, final)
    time.sleep(2.0)
    # save progress after each attempt
    with OUT_PATH.open('w', encoding='utf-8', newline='') as outf:
        writer = csv.DictWriter(outf, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

print('finished retry run, wrote', OUT_PATH)
print('blog 200', sum(1 for r in rows if r['blog_status']=='200'))
print('blog error', sum(1 for r in rows if r['blog_status']!='200'))
