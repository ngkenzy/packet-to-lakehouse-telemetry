# Case Study — Packet-to-Lakehouse Telemetry

## Problem
Network packet captures (`pcap`) are rich in detail but stored in binary formats that are hard to query at scale. Analysts need fast, SQL-based ways to extract insights like top talkers, latency, and retransmissions.

## Scenario
- **Input:** Synthetic 500 MB `pcap` (~5M packets)  
- **Pipeline:** tshark → CSV → DuckDB/Parquet → SQL queries  
- **Queries:** top talkers, port usage, RTT, retransmissions  
- **Hardware:** Single Linux VM (2 vCPU, 4 GB RAM)

## Results
- **Conversion time:** 3 min (pcap → CSV → Parquet)  
- **Query speed:**  
  - CSV: ~2.3s (1M rows)  
  - Parquet: ~0.15s (1M rows)  
- **Top talkers:** Exported as CSV + chart (example)  
- **RTT (avg):** ~24 ms  
- **Retransmissions:** <0.5% of flows  

## Lessons
- **Columnar storage (Parquet)** drastically improves query speed & reduces storage.  
- **Automation** via Python scripts makes pipeline repeatable for any `pcap`.  
- **Failure modes:** Missing fields in tshark export can break downstream schema — solved with schema normalization in `csv_to_parquet.py`.  
- **Key takeaway:** Treating packet captures as lakehouse data enables fast, interactive analytics instead of manual packet inspection.
