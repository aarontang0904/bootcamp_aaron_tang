# Data Storage (Stage 05)

- **Folders:** `data/raw/` holds CSV snapshots (raw); `data/processed/` holds Parquet files (processed).
- **Formats:** CSV for portability; Parquet for efficient, typed storage and faster I/O.
- **Env paths:** `.env` can define `DATA_DIR_RAW` and `DATA_DIR_PROCESSED`; defaults used if unset.
- **Utilities:** `write_df` / `read_df` handle `.csv` and `.parquet`, manage directories, and validate.
