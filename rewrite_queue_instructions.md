# Rewrite Queue Instructions

## Source queue

Use:

- [below_1000_words_blogs_live_confirmed_548.csv](/Users/rakeshanita/Downloads/Legal%20Suvidha%20Content%20Upgrade%20for%20AI%20Search%20Visibility/below_1000_words_blogs_live_confirmed_548.csv:1)

## Production scaffold

Use:

- [rewrite_queue_template.csv](/Users/rakeshanita/Downloads/Legal%20Suvidha%20Content%20Upgrade%20for%20AI%20Search%20Visibility/rewrite_queue_template.csv:1)
- [rewrite_prompt_production.txt](/Users/rakeshanita/Downloads/Legal%20Suvidha%20Content%20Upgrade%20for%20AI%20Search%20Visibility/rewrite_prompt_production.txt:1)

## How to use it

1. Start from one confirmed live row in `below_1000_words_blogs_live_confirmed_548.csv`.
2. Copy the provenance columns into the matching template fields.
3. Fill these rewrite-input fields:
   - `TITLE`
   - `GEO_SCOPE`
   - `LOCATION`
   - `TARGET_KEYWORDS`
   - `RELATED_TERMS`
   - `SEARCH_INTENT`
   - `ORIGINAL_CONTENT`
4. Set `SOURCE_URL` to the live canonical blog URL.
5. Set `STATUS` to one of:
   - `READY_FOR_REWRITE`
   - `IN_PROGRESS`
   - `REVIEW`
   - `APPROVED`
   - `PUBLISHED`
6. Run the prompt from `rewrite_prompt_production.txt`.
7. Save the generated output into:
   - `REWRITE_TEXT`
   - `REWRITE_DRAFT` (optional plain-text or review copy if you still want it)
   - `SEO_TITLE`
   - `META_DESCRIPTION`
   - `INTERNAL_LINK_ANCHORS`
8. Use `NOTES` for merge decisions, redirect notes, author guidance, or CTA instructions.

## Recommended column roles

### Queue provenance

- `title`
- `words`
- `date`
- `year`
- `categories`
- `seo_score`
- `focus_keyword`
- `url`
- `slug`
- `orig_url`
- `blog_url`
- `orig_status`
- `orig_final_url`
- `blog_status`
- `blog_final_url`
- `checked`

### Rewrite production fields

- `TITLE`
- `GEO_SCOPE`
- `LOCATION`
- `TARGET_KEYWORDS`
- `RELATED_TERMS`
- `SEARCH_INTENT`
- `ORIGINAL_CONTENT`
- `SOURCE_URL`
- `CATEGORY`
- `WORD_COUNT`
- `STATUS`
- `REWRITE_DRAFT`
- `REWRITE_TEXT`
- `SEO_TITLE`
- `META_DESCRIPTION`
- `INTERNAL_LINK_ANCHORS`
- `PRIMARY_INTERNAL_LINKS`
- `SUPPORTING_INTERNAL_LINKS`
- `CTA_LINK_TARGET`
- `NOTES`

## Practical note

The prompt is applied row-by-row to article content.

It is not a spreadsheet formula.

## Publishing format

Primary publishable output:

- `REWRITE_TEXT`

Recommended use:

- keep `ORIGINAL_CONTENT` unchanged for source reference
- generate clean WordPress-safe plain text into `REWRITE_TEXT`
- use `SEO_TITLE`, `META_DESCRIPTION`, and `INTERNAL_LINK_ANCHORS` separately
- treat `REWRITE_DRAFT` as optional review text if needed

## Geo model

Use an India-first geo strategy:

- `NATIONAL`: default for most compliance, filing, penalty, checklist, and applicability pages
- `LOCAL`: only for strongly city-led service pages
- `HYBRID`: India-wide core content with selective local examples
