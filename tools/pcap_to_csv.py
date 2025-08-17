import sys, os, csv
import pyshark

pcap, out_csv = sys.argv[1], sys.argv[2]
cap = pyshark.FileCapture(pcap, only_summaries=True)
os.makedirs(os.path.dirname(out_csv), exist_ok=True)
with open(out_csv, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['time','src','dst','protocol','length','info'])
    for pkt in cap:
        w.writerow([pkt.time, pkt.source, pkt.destination, pkt.protocol, pkt.length, pkt.info])
print(f"[+] wrote {out_csv}")
