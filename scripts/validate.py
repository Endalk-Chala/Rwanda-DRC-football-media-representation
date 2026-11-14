#!/usr/bin/env python3
import csv
import datetime
from pathlib import Path
from urllib.parse import urlsplit

file = Path(__file__).resolve().parents[1] / "data/government_source_register.csv"
with file.open(encoding="utf-8-sig", newline="") as handle:
    rows = list(csv.DictReader(handle))
assert len({r["record_id"] for r in rows}) == len(rows), "Duplicate IDs"
assert len({r["source_url"] for r in rows}) == len(rows), "Duplicate URLs"
for r in rows:
    datetime.date.fromisoformat(r["publication_date"])
    assert urlsplit(r["source_url"]).scheme == "https"
    assert r["coding_status"] == "not_coded"
    assert r["country"] in {"RWA", "DRC"}
print(f'PASS: {len(rows)} candidate records. This does not check live URL content.')
