# Developer Import Format

The developer import file must use exactly these four headers:

```text
Post id,Slug,Title,Content
```

## File To Use

Use:

- `developer_blog_update_text_only.csv`

This file is intentionally limited to rows that pass the minimum content requirement.

## Minimum Content Rule

Only include rows where:

- `Content` is plain text only.
- `Content` has at least `2,500` words.
- `Content` is AEO-ready, SEO-ready, India-first or geo-appropriate, and AI-search-visibility ready.

## QA File

Use:

- `developer_blog_update_needs_expansion.csv`

This file lists completed text rewrites that are still below the `2,500` word requirement and should not be imported yet.

## Mapping From Master Workbook

Map fields as follows:

- `Post id` = WordPress post ID from the original post export.
- `Slug` = `slug`
- `Title` = `TITLE` or `title`
- `Content` = `REWRITE_TEXT`

## Important

Do not import from `REWRITE_HTML`.

The developer-ready field is:

- `REWRITE_TEXT`

