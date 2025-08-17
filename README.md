# Packet-to-Lakehouse Telemetry

**Story:** Convert captured packets into analytics-ready columnar data, then run fast SQL to find top talkers, RTT, and retransmissions.

## Pipeline
pcap → (tshark) CSV → (DuckDB/Python) Parquet → SQL queries → charts/dashboard

## Quickstart
```bash
# 0) prerequisites: Python 3.10+, tshark, DuckDB (python package)
pip install -r requirements.txt

# 1) demo dataset
./capture_demo.sh   # creates demo.pcap (synthetic)
python tools/pcap_to_csv.py data/demo.pcap data/flows.csv
python tools/csv_to_parquet.py data/flows.csv data/flows.parquet

# 2) analytics
python tools/queries.py data/flows.parquet outputs/

# 3) open outputs/ for CSVs; visualize in your tool of choice
```

## What to show in the README
- SQL queries for top talkers, port usage, average RTT, retransmissions
- Cost/perf notes: CSV vs Parquet query times
- A screenshot of a small dashboard (optional)
