import sys, os, duckdb, pandas as pd

parquet = sys.argv[1]
outdir = sys.argv[2]
os.makedirs(outdir, exist_ok=True)

con = duckdb.connect()
con.execute("CREATE VIEW flows AS SELECT * FROM parquet_scan(?)", [parquet])

# Example queries
q_top_talkers = "SELECT src, COUNT(*) cnt FROM flows GROUP BY src ORDER BY cnt DESC LIMIT 20"
q_proto = "SELECT protocol, COUNT(*) cnt FROM flows GROUP BY protocol ORDER BY cnt DESC"
q_lengths = "SELECT CAST(length AS INT) len, COUNT(*) cnt FROM flows GROUP BY len ORDER BY cnt DESC LIMIT 50"

for name, q in [('top_talkers', q_top_talkers), ('by_protocol', q_proto), ('length_hist', q_lengths)]:
    df = con.execute(q).df()
    df.to_csv(os.path.join(outdir, f'{name}.csv'), index=False)

print(f"[+] wrote CSVs to {outdir}")
