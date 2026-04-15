# Legal Suvidha: Live + Backup Verified Inventory

## What has been verified

### Backup snapshot

- Source: `public_html/wp-content/uploads/wpallimport/files/Posts_Export_2025_June_26_0803.csv`
- Verified post rows: `919`
- Source: `public_html/wp-content/uploads/wpallimport/files/Posts_Export_2025_June_25_1922.csv`
- Verified post rows: `919`
- Matching XML node count for both post exports: `919`
- Service export rows: `247`

### ZIP file

- ZIP contains the same post export files and service export files
- Checksum of `Posts_Export_2025_June_26_0803.csv` inside ZIP matches the extracted copy exactly
- Conclusion: the ZIP is not a different content snapshot for the exported posts we audited

## Important correction

The `919` figure is valid for the exported backup post dataset.

It should **not** be treated as the final live-site content total without qualification.

## Why

The live site shows a newer public content layer that is not fully reflected in the backup export we analyzed.

Verified live signals include:

- `https://legalsuvidha.com/blogs/`
- newer 2025 and 2026 blog content on `/blog/`
- newer legal, tax, startup, property, and compliance articles visible on the public site

This means:

- backup export total: known
- live total blog count: not yet fully enumerated from public discovery alone

## Best current understanding

- `919` exported post records in the backup
- `247` exported service records in the backup
- live site likely contains content beyond the backup export
- therefore the real live content universe is larger than the export-only view

## Public site observations verified

### Homepage

The homepage is strongly conversion-oriented and service-led, with broad coverage across:

- company registration
- GST
- IP
- ROC compliance
- income tax
- NRI services
- startup legal
- family law
- criminal defence
- property law
- MSME / labour
- import/export

### Blog hub

The public blog hub at `/blogs/` shows active publication into 2026, including:

- GST notice response
- prosecution under GST
- GST audit risk/red flags
- GST judgments

### Newer high-intent live content

The live site visibly contains newer-style articles with:

- narrative hooks
- penalty/risk framing
- author blocks
- last updated fields
- table of contents
- stronger CTA placement

## Working implication for our audit

We should now treat the project in two layers:

### Layer 1: Backup-export content

Use this for:

- large-scale content audit
- weak blog detection
- duplicate/cannibalization discovery
- first rewrite backlog generation

### Layer 2: Live public content

Use this for:

- current messaging verification
- proof of newer content style
- calibration of what “good current pages” look like
- identifying active content clusters worth expanding

## First 10 draft upgrade candidates from the verified backup layer

These remain strong starting points because they are:

- commercially relevant
- structurally weak or thin
- easy to rewrite into AEO/GEO/SEO-ready pages

1. `Annual Compliances of LLP`
2. `LLP Annual Filing & Compliance Guide`
3. `ROC compliance checklist: Key Guide`
4. `Procedure of Enrollment of GST`
5. `The Registration Process under GST Section 68: How to Enroll for GST`
6. `Applicability of GST on GTA`
7. `Trademark`
8. `LLP Annual Filing: 10 Avoidable Errors`
9. `ROC Compliance for Companies & LLPs`
10. `How to take advantage of the amnesty for GST registration`

## Next verification step

To make the first batch fully defensible, the next step is:

- enumerate publicly discoverable live blog URLs
- match them against the backup export
- mark each candidate as:
  - live and current
  - live but outdated
  - redirected / changed
  - missing from live layer

That will let us finalize the first 10 pages with confidence before rewriting.
