#!/usr/bin/env python3
"""Structural checks for every register in data/.

Checks field structure only: unique IDs and URLs, HTTPS links, date formats,
allowed codes, and cross-references between files. It does not open any URL
and does not test whether a source is valid, live, relevant, or complete.

Usage: python scripts/validate.py
Exit code 0 if no errors (warnings allowed), 1 if any error.
"""
import csv
import datetime
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

DATA = Path(__file__).resolve().parents[1] / "data"
STUDY_START = "2018-01-01"
STUDY_END = "2026-11-13"

errors = []
warnings = []


def load(name):
    with (DATA / name).open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def check_unique(name, rows, field):
    seen = set()
    for r in rows:
        value = r[field].strip()
        if value in seen:
            errors.append(f"{name}: duplicate {field} {value!r}")
        seen.add(value)


def check_url(name, rid, url):
    parts = urlsplit(url.strip())
    if parts.scheme != "https" or not parts.netloc:
        errors.append(f"{name}: {rid} source_url is not a full https link")


def check_date(name, rid, value, allow_partial=False, allow_blank=False):
    """Accept YYYY-MM-DD; optionally YYYY-MM, YYYY, or blank."""
    value = value.strip()
    if not value:
        if not allow_blank:
            errors.append(f"{name}: {rid} has no publication date")
        return
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        try:
            datetime.date.fromisoformat(value)
        except ValueError:
            errors.append(f"{name}: {rid} has an impossible date {value!r}")
            return
        if value < STUDY_START or value > STUDY_END:
            warnings.append(
                f"{name}: {rid} dated {value}, outside the study period "
                f"{STUDY_START} to {STUDY_END}"
            )
        return
    if allow_partial and re.fullmatch(r"\d{4}(-(0[1-9]|1[0-2]))?", value):
        year = value[:4]
        if year < STUDY_START[:4] or year > STUDY_END[:4]:
            warnings.append(f"{name}: {rid} dated {value}, outside the study period")
        return
    errors.append(f"{name}: {rid} has a badly formatted date {value!r}")


def check_code(name, rid, field, value, allowed):
    if value not in allowed:
        errors.append(f"{name}: {rid} {field}={value!r} not in {sorted(allowed)}")


def check_filled(name, rows, id_field, fields):
    for r in rows:
        for f in fields:
            if not r[f].strip():
                errors.append(f"{name}: {r[id_field]} has an empty {f}")


# Corpus 1: government communications
GOV = "government_source_register.csv"
gov = load(GOV)
check_unique(GOV, gov, "record_id")
check_unique(GOV, gov, "source_url")
check_filled(GOV, gov, "record_id", ["original_title", "partner_club", "source_review_status"])
for r in gov:
    rid = r["record_id"]
    check_date(GOV, rid, r["publication_date"])
    check_url(GOV, rid, r["source_url"])
    check_code(GOV, rid, "country", r["country"], {"RWA", "DRC"})
    check_code(GOV, rid, "original_language", r["original_language"], {"en", "fr"})
    check_code(GOV, rid, "coding_status", r["coding_status"], {"not_coded"})
    if not rid.startswith(f"GOV-{r['country']}-"):
        errors.append(f"{GOV}: {rid} does not match its country code {r['country']}")

# Page-level audit of government records
AUDIT = "verification_audit_v0.3.csv"
audit = load(AUDIT)
check_unique(AUDIT, audit, "record_id")
gov_by_id = {r["record_id"]: r for r in gov}
for r in audit:
    rid = r["record_id"]
    if rid not in gov_by_id:
        errors.append(f"{AUDIT}: {rid} is not in the government register")
        continue
    check_date(AUDIT, rid, r["on_page_date_confirmed"])
    check_date(AUDIT, rid, r["audit_date"])
    if r["on_page_date_confirmed"] != gov_by_id[rid]["publication_date"]:
        warnings.append(
            f"{AUDIT}: {rid} audited date {r['on_page_date_confirmed']} differs from "
            f"register date {gov_by_id[rid]['publication_date']}"
        )
    domain = urlsplit(gov_by_id[rid]["source_url"]).netloc.removeprefix("www.")
    if domain != r["original_domain"]:
        warnings.append(
            f"{AUDIT}: {rid} audit domain {r['original_domain']} differs from "
            f"register URL domain {domain}"
        )
inspected = {r["record_id"] for r in gov if r["source_review_status"].startswith("page_content_inspected")}
audited = {r["record_id"] for r in audit}
if inspected != audited:
    errors.append(
        f"{AUDIT}: audited records and register records marked inspected do not match "
        f"(only in audit: {sorted(audited - inspected)}; only in register: {sorted(inspected - audited)})"
    )

# Corpus 2: European club communications
CLUB = "club_communications_discovery_v0.1.csv"
club = load(CLUB)
check_unique(CLUB, club, "record_id")
check_unique(CLUB, club, "source_url")
check_filled(CLUB, club, "record_id", ["club", "title", "language", "genre", "event_key", "verification_status"])
club_ids = {r["record_id"] for r in club}
for r in club:
    rid = r["record_id"]
    check_url(CLUB, rid, r["source_url"])
    check_code(CLUB, rid, "country", r["country"], {"RWA", "DRC"})
    check_code(CLUB, rid, "date_precision", r["date_precision"], {"day", "inferred_day", "undated", "date_check"})
    check_code(CLUB, rid, "relation_to_partnership", r["relation_to_partnership"], {"direct", "incidental"})
    if r["date_precision"] in ("day", "inferred_day"):
        check_date(CLUB, rid, r["publication_date"])
    elif r["publication_date"].strip():
        check_date(CLUB, rid, r["publication_date"], allow_partial=True)
    if not r["event_key"].startswith(r["country"] + "-"):
        errors.append(f"{CLUB}: {rid} event_key {r['event_key']} does not match country {r['country']}")
    pair = r["alternate_version_or_pair"].strip()
    if re.fullmatch(r"[A-Z]+(-[A-Z]+)*-\d+", pair) and pair not in club_ids:
        warnings.append(f"{CLUB}: {rid} points to paired record {pair!r}, which is not a record_id in this file")

# Corpus 3a: African press
AFR = "african_journalistic_coverage_discovery_v0.1.csv"
afr = load(AFR)
check_unique(AFR, afr, "record_id")
check_unique(AFR, afr, "source_url")
check_filled(AFR, afr, "record_id", ["outlet", "outlet_location", "title", "event_key", "clubs", "genre"])
for r in afr:
    rid = r["record_id"]
    check_url(AFR, rid, r["source_url"])
    check_date(AFR, rid, r["publication_date"], allow_partial=True)
    check_code(AFR, rid, "case_focus", r["case_focus"], {"RWA", "DRC", "REG"})

# Corpus 3b: international press
INT = "international_journalism_discovery_v0.1.csv"
intl = load(INT)
check_unique(INT, intl, "record_id")
check_unique(INT, intl, "source_url")
check_filled(INT, intl, "record_id", ["publisher", "title", "event_key", "sampling_tier", "origin_check"])
for r in intl:
    rid = r["record_id"]
    check_url(INT, rid, r["source_url"])
    check_date(INT, rid, r["publication_date"], allow_partial=True)
    check_code(INT, rid, "case_focus", r["case_focus"], {"RWA", "DRC", "BOTH"})
    check_code(INT, rid, "press_region", r["press_region"], {"UK", "France", "Italy", "Germany", "Spain", "USA"})
    check_code(INT, rid, "genre_coding", r["genre_coding"], {"not_coded"})
    check_code(INT, rid, "frame_coding", r["frame_coding"], {"not_coded"})

# Supplementary reports and boundary sources
SUP = "supplementary_official_reports_and_boundary_sources.csv"
sup = load(SUP)
check_unique(SUP, sup, "document_id")
check_unique(SUP, sup, "source_url")
for r in sup:
    check_url(SUP, r["document_id"], r["source_url"])
    check_code(SUP, r["document_id"], "country", r["country"], {"RWA", "DRC"})
    if not re.fullmatch(r"\d{4}", r["report_year_or_event_year"]):
        errors.append(f"{SUP}: {r['document_id']} year is not YYYY")

# Page-level check of the two communication corpora
VER = "communication_verification_2026-11-19.csv"
ver = load(VER)
check_unique(VER, ver, "record_id")
expected_ids = {r["record_id"] for r in gov} | {r["record_id"] for r in club}
ver_ids = {r["record_id"] for r in ver}
if ver_ids != expected_ids:
    errors.append(
        f"{VER}: records do not match the government and club registers "
        f"(missing: {sorted(expected_ids - ver_ids)}; extra: {sorted(ver_ids - expected_ids)})"
    )
register_dates = {r["record_id"]: r["publication_date"] for r in gov + club}
for r in ver:
    rid = r["record_id"]
    check_code(VER, rid, "page_read", r["page_read"], {"yes", "no"})
    if r["date_on_page"] and r["date_on_page"] != register_dates.get(rid):
        errors.append(
            f"{VER}: {rid} date on page {r['date_on_page']} differs from "
            f"register date {register_dates.get(rid)!r}"
        )
open_flags = sum(1 for r in ver if r["flag"].strip())

# The same URL should not sit in two registers
seen_urls = {}
for name, rows, id_field in [
    (GOV, gov, "record_id"), (CLUB, club, "record_id"), (AFR, afr, "record_id"),
    (INT, intl, "record_id"), (SUP, sup, "document_id"),
]:
    for r in rows:
        url = r["source_url"].strip().rstrip("/")
        if url in seen_urls and seen_urls[url][0] != name:
            warnings.append(f"same URL in {seen_urls[url][0]} ({seen_urls[url][1]}) and {name} ({r[id_field]})")
        seen_urls.setdefault(url, (name, r[id_field]))

# Event keys used by the press but not shared across registers (information only)
press_only = sorted(
    ({r["event_key"] for r in afr} ^ {r["event_key"] for r in intl})
)

print("Records checked:")
for label, rows in [
    ("government", gov), ("government audit", audit), ("club", club),
    ("African press", afr), ("international press", intl), ("supplementary", sup),
    ("communication verification", ver),
]:
    print(f"  {label}: {len(rows)}")
print(f"  corpus total (government + club + press): {len(gov) + len(club) + len(afr) + len(intl)}")
print(f"\nCommunication records with an open verification flag: {open_flags} of {len(ver)}")
print(f"\nEvent keys used in only one of the two press registers: {len(press_only)}")
for key in press_only:
    print(f"  {key}")
print(f"\nWarnings: {len(warnings)}")
for w in warnings:
    print(f"  WARNING {w}")
print(f"\nErrors: {len(errors)}")
for e in errors:
    print(f"  ERROR {e}")
if errors:
    print("\nFAIL: fix the errors above.")
    sys.exit(1)
print("\nPASS: field structure is consistent. This does not check live URL content, source validity, or completeness.")
