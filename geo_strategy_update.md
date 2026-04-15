# India-Wide Geo Strategy Update

## What changed

The rewrite workflow has been updated from a Delhi NCR-default model to an India-first geo model.

## New field

- `GEO_SCOPE`

Allowed values:

- `NATIONAL`
- `LOCAL`
- `HYBRID`

## Default rule

Most Legal Suvidha content should now be written as:

- `GEO_SCOPE = NATIONAL`
- `LOCATION = India`

This is the right default for:

- LLP compliance
- ROC compliance
- annual filing
- GST compliance
- DIR-3 KYC
- DPT-3
- trademark registration
- Startup India and MSME content
- most checklist and penalty pages

## When to use LOCAL

Use `LOCAL` only when:

- the page is strongly city-led
- the service query naturally includes city modifiers
- local trust signals improve conversion

## When to use HYBRID

Use `HYBRID` where the article should primarily work nationwide but also benefits from practical local examples.

Examples:

- home bakers
- Swiggy vendors
- Amazon warehouse compliance
- operational service pages with regional execution context

## Files updated

- all rewrite queue CSV files
- `master_rewrite_workbook.csv`
- `master_rewrite_workbook.xlsx`
- `rewrite_prompt_production.txt`
- `rewrite_queue_instructions.md`
- `rewrite_queue_batch_manifest.md`

## Publishing recommendation

Use:

- `REWRITE_HTML` as the main WordPress replacement body

Keep:

- `ORIGINAL_CONTENT` for reference
- `REWRITE_DRAFT` only if you want a review copy separate from the final HTML
