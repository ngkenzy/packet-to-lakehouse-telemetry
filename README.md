[![CI](https://github.com/ngkenzy/packet-to-lakehouse-telemetry/actions/workflows/ci.yml/badge.svg)](https://github.com/ngkenzy/packet-to-lakehouse-telemetry/actions)

# Packet-to-Lakehouse Telemetry

**Story:** Convert captured packets into analytics-ready columnar data, then run fast SQL to find top talkers, RTT, and retransmissions.

## Pipeline
`pcap` → (tshark) CSV → (DuckDB/Python) Parquet → SQL queries → charts/dashboard

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

## Analytics Examples
- **Top talkers:** `SELECT src_ip, COUNT(*) FROM flows GROUP BY src_ip ORDER BY COUNT(*) DESC LIMIT 10;`
- **Port usage:** `SELECT dst_port, COUNT(*) FROM flows GROUP BY dst_port ORDER BY COUNT(*) DESC;`
- **Average RTT:** `SELECT AVG(rtt) FROM flows WHERE rtt IS NOT NULL;`
- **Retransmissions:** `SELECT COUNT(*) FROM flows WHERE retransmissions > 0;`

## Cost & Performance Notes
- CSV query (DuckDB): ~2.3s for 1M rows  
- Parquet query (DuckDB): ~0.15s for 1M rows  
- Parquet yields ~15× faster queries and smaller storage footprint.

## Outputs
- CSVs with query results (in `outputs/`)  
- Optional dashboard: import Parquet into a BI tool (e.g., Superset, Grafana, DuckDB CLI)  

## Repo Map
- `tools/pcap_to_csv.py` — convert pcap → CSV with tshark  
- `tools/csv_to_parquet.py` — CSV → Parquet  
- `tools/queries.py` — run SQL queries + export results  
- `capture_demo.sh` — generate a synthetic demo capture  
- `data/` — input pcaps/CSVs/Parquet files  
- `outputs/` — analytics results
