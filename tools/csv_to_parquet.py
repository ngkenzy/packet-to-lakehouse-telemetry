import sys
import pandas as pd
import duckdb

csv_in, parquet_out = sys.argv[1], sys.argv[2]
df = pd.read_csv(csv_in)
duckdb.sql("COPY df TO ? (FORMAT PARQUET)", [parquet_out])
print(f"[+] wrote {parquet_out}")
