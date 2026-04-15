# Rewrite Queue Batch Manifest

Source queue:

- [below_1000_words_blogs_live_confirmed_548.csv](/Users/rakeshanita/Downloads/Legal%20Suvidha%20Content%20Upgrade%20for%20AI%20Search%20Visibility/below_1000_words_blogs_live_confirmed_548.csv:1)

## Prepared batches

- Rows `1–10`:
  - [rewrite_queue_first_10.csv](/Users/rakeshanita/Downloads/Legal%20Suvidha%20Content%20Upgrade%20for%20AI%20Search%20Visibility/rewrite_queue_first_10.csv:1)
- Rows `11–20`:
  - [rewrite_queue_11_20.csv](/Users/rakeshanita/Downloads/Legal%20Suvidha%20Content%20Upgrade%20for%20AI%20Search%20Visibility/rewrite_queue_11_20.csv:1)
- Rows `21–30`:
  - [rewrite_queue_21_30.csv](/Users/rakeshanita/Downloads/Legal%20Suvidha%20Content%20Upgrade%20for%20AI%20Search%20Visibility/rewrite_queue_21_30.csv:1)
- Rows `31–60`:
  - [rewrite_queue_31_60.csv](/Users/rakeshanita/Downloads/Legal%20Suvidha%20Content%20Upgrade%20for%20AI%20Search%20Visibility/rewrite_queue_31_60.csv:1)
- Rows `61–120`:
  - [rewrite_queue_61_120.csv](/Users/rakeshanita/Downloads/Legal%20Suvidha%20Content%20Upgrade%20for%20AI%20Search%20Visibility/rewrite_queue_61_120.csv:1)
- Rows `121–260`:
  - [rewrite_queue_121_260.csv](/Users/rakeshanita/Downloads/Legal%20Suvidha%20Content%20Upgrade%20for%20AI%20Search%20Visibility/rewrite_queue_121_260.csv:1)
- Rows `261–450`:
  - [rewrite_queue_261_450.csv](/Users/rakeshanita/Downloads/Legal%20Suvidha%20Content%20Upgrade%20for%20AI%20Search%20Visibility/rewrite_queue_261_450.csv:1)
- Rows `451–548`:
  - [rewrite_queue_451_548.csv](/Users/rakeshanita/Downloads/Legal%20Suvidha%20Content%20Upgrade%20for%20AI%20Search%20Visibility/rewrite_queue_451_548.csv:1)

## Count check

- `1–10`: `10`
- `11–20`: `10`
- `21–30`: `10`
- `31–60`: `30`
- `61–120`: `60`
- `121–260`: `140`
- `261–450`: `190`
- `451–548`: `98`

Total prepared rows: `548`

## Notes

- Each batch uses the same prompt-ready schema.
- Each row includes:
  - live-confirmed queue provenance
  - geo scope
  - suggested location
  - target keywords
  - related terms
  - search intent
  - source URL
  - source article content in `ORIGINAL_CONTENT`
  - internal-link planning fields
  - workflow status placeholders
- Rows `21–548` were prepared with auto-generated metadata fields, so canonical overlap decisions should still be reviewed before final publishing.
- The workbook now follows an India-first geo strategy instead of forcing `Delhi NCR` across all pages.
