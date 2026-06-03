import argparse
import json
import time

parser = argparse.ArgumentParser(description='Switch Monitoring')
parser.add_argument("bridge", default="s1", help="OVS bridge name (default: s1)")
parser.add_argument("--interval", type=float, default=1.0, help="Poll interval in seconds (default 1.0)")
parser.add_argument("--out", default="stats")
args = parser.parse_args()

stats_data = {
    "bridge": args.bridge,
    "interval": args.interval,
    "samples": [],
    "events": []
}