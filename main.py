"""Summarise Wi-Fi signal samples per access point.

Usage: python3 main.py samples.csv
CSV columns: ap,timestamp,signal_dbm.
Per AP: sample count, average signal, weakest sample. WEAK if the
average is below -70 dBm. Weakest average first.
"""
import argparse, csv, sys
from collections import defaultdict


def analyze(rows):
    samples = defaultdict(list)
    for row in rows:
        samples[row["ap"].strip()].append(int(row["signal_dbm"]))
    out = []
    for ap, values in samples.items():
        avg = sum(values) / len(values)
        verdict = "WEAK" if avg < -70 else "OK"
        out.append((ap, len(values), avg, min(values), verdict))
    return sorted(out, key=lambda r: r[2])


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    args = parser.parse_args(argv)
    with open(args.path, newline="", encoding="utf-8") as f:
        for ap, count, avg, weakest, verdict in analyze(list(csv.DictReader(f))):
            print(f"{ap}: {verdict} (avg {avg:.0f} dBm, weakest {weakest} dBm, {count} samples)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
