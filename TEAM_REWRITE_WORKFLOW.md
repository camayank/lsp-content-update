# Legal Suvidha Rewrite Team Workflow

This file is the shared operating guide for rewriting the Legal Suvidha blog queue with consistent quality, AEO, SEO, India-wide relevance, and internal linking.



## Exact File And Column References

Primary source file for all team members:

- `master_rewrite_workbook.csv`

Optional spreadsheet version:

- `master_rewrite_workbook.xlsx`

Assignment tracker:

- `team_rewrite_assignments.csv`

Prompt file:

- `rewrite_prompt_production.txt`

Developer import file:

- `developer_blog_update_text_only.csv`

Rows below 2,500 words must stay out of the developer import file and should be tracked in:

- `developer_blog_update_needs_expansion.csv`

Actual source/reference columns available in `master_rewrite_workbook.csv`:

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
- `TITLE`
- `GEO_SCOPE`
- `LOCATION`
- `TARGET_KEYWORDS`
- `RELATED_TERMS`
- `SEARCH_INTENT`
- `PRIMARY_INTERNAL_LINKS`
- `SUPPORTING_INTERNAL_LINKS`
- `CTA_LINK_TARGET`
- `ORIGINAL_CONTENT`
- `SOURCE_URL`
- `CATEGORY`
- `WORD_COUNT`
- `NOTES`
- `SOURCE_BATCH`

Important: `master_rewrite_workbook.csv` does not currently contain WordPress post IDs for all 548 rows. Use `slug` as the stable matching key. Do not invent a `Post id`.

Write these output columns in `master_rewrite_workbook.csv`:

- `REWRITE_TEXT`
- `SEO_TITLE`
- `META_DESCRIPTION`
- `INTERNAL_LINK_ANCHORS`
- `STATUS`
- `NOTES`, only for important concerns

Developer import mapping:

- `Post id` = mapped WordPress post ID only when available from an existing WordPress export or developer mapping
- `Slug` = `slug`
- `Title` = improved final title
- `Content` = `REWRITE_TEXT`

If `Post id` is unavailable, keep the row matched by `Slug` and ask the developer to map the WordPress ID by slug during import.

## Source Of Truth

Use only:

- `master_rewrite_workbook.csv`
- `master_rewrite_workbook.xlsx`

The developer-ready content field is:

- `REWRITE_TEXT`

Do not use `REWRITE_HTML` for new work unless specifically requested. It is kept only as a backup from the earlier workflow.

## Current Status

- Total rewrite rows: `548`
- Completed/review-ready rows so far: `13`
- Remaining rows: `535`

## Required Output Fields

Each completed row must fill:

- `REWRITE_TEXT`
- `SEO_TITLE`
- `META_DESCRIPTION`
- `INTERNAL_LINK_ANCHORS`
- `STATUS`

Use `STATUS = REVIEW` when the row is ready for review.

## Shared Prompt

Use the prompt in:

- `rewrite_prompt_production.txt`

The prompt is now text-only. Do not generate HTML.

## Quality Rules

Every rewrite must:

- Be at least `2,500` words unless the reviewer explicitly approves a shorter strategic page.
- Use plain text only, with heading labels like `H1:`, `H2:`, and `H3:`.
- Start with a direct answer in the first `80` words.
- Include AEO-friendly answer boxes using plain text labels like `Answer Box:`.
- Use `2026` framing where old years are mentioned.
- Update outdated references instead of preserving old-year wording.
- Use cautious language for temporary schemes, due dates, fees, penalties, and regulatory positions unless verified.
- Be India-first by default unless `GEO_SCOPE` says `LOCAL` or `HYBRID`.
- Include internal-link anchor text naturally from the internal-link fields.
- Include a practical CTA aligned with the search intent.
- Avoid copying phrases from the original article.

## AEO Requirements

Each article should include:

- A direct answer opening.
- At least one answer box.
- Practical checklists or step lists.
- A consequence/risk section where relevant.
- A next-step section.
- `6-8` FAQs with useful answers.

## SEO Requirements

Each article should include:

- Primary keyword in the title/opening naturally.
- Semantic variations throughout the article.
- Search-intent-specific sections.
- A unique page angle to avoid cannibalization.
- `SEO_TITLE` under roughly `70` characters where possible.
- `META_DESCRIPTION` under roughly `160` characters where possible.

## Internal Linking Requirements

Use the workbook fields:

- `PRIMARY_INTERNAL_LINKS`
- `SUPPORTING_INTERNAL_LINKS`
- `CTA_LINK_TARGET`

Rules:

- Include `3-6` natural internal-link anchor mentions in the article.
- Use descriptive anchor text.
- Do not use raw URLs unless a URL is already supplied.
- Link to the next logical reader question, not random pages.

## 2026 Update Rule

When source content mentions old years such as `2021`, `2022`, `2023`, `2024`, or `2025`:

- Update the framing to `2026` where appropriate.
- Remove stale one-time scheme language unless still verified.
- Keep historical facts only when clearly marked as historical context.
- For legal/tax/compliance facts that may change, verify from official sources before writing.

## Team Assignment Process

Use:

- `team_rewrite_assignments.csv`

Recommended process:

1. Pick an unassigned batch.
2. Add your name in the `OWNER` column.
3. Work only on rows within that batch.
4. Fill `REWRITE_TEXT` and SEO fields in the master workbook.
5. Set row `STATUS = REVIEW`.
6. Add concerns in `NOTES`.

## Review Checklist

Before marking a row as `REVIEW`, confirm:

- No HTML tags are present in `REWRITE_TEXT`.
- The article is not a shallow expansion of the original.
- Old years are updated or contextualized.
- Temporary schemes are not presented as currently active unless verified.
- Internal links are relevant.
- The page has a distinct search intent.
- SEO title and meta description are filled.
