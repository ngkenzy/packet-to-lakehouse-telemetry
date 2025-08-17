#!/usr/bin/env bash
set -euo pipefail
mkdir -p data
# Create a tiny synthetic pcap by generating ping/iperf traffic between namespaces or localhost
# If tshark is installed, this will capture 3 seconds of loopback traffic as a demo
timeout 3s tshark -i lo -w data/demo.pcap || echo "Skipping live capture; ensure tshark and permissions are available."
echo "[+] Wrote data/demo.pcap (if capture succeeded)"
