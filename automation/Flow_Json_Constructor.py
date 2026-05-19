import argparse
import json

parser = argparse.ArgumentParser(description="Generate ODL flow rules")
parser.add_argument("--flow-id", required=True)
parser.add_argument("--priority", type=int, default=500)
parser.add_argument("--table-id", type=int, default=0)
parser.add_argument("--src_ip")
parser.add_argument("--in_port")
parser.add_argument("--action", default="NORMAL", help="NORMAL, DROP, or output:<port>")

args = parser.parse_args()

def construct_match(src_ip=None, in_port=None):
    match = {}
    if src_ip != None:
        match["ip-match"] = {}
        match["ipv4-source"] = args.src_ip
    if in_port != None:
        match["in-port"] = args.in_port
    return match

actions = []
if args.action == "NORMAL":
    actions.append({
        "order": 0,
        "output-action": {
            "output-node-connector": "NORMAL"
        }
    })
elif args.action == "DROP":
    actions.append({
        "order": 0,
        "drop-action": {}
    })
elif args.action and args.action.startswith("output:"):
    port = args.action.split(":")[1]
    actions.append({
        "order": 0,
        "output-action": {
            "output-node-connector": port
        }
    })

instructions = {
    "instruction": [{
        "order": 0,
        "apply-actions": {
            "action": actions
        }
    }]
}

def build_flow(flow_id, priority, table_id, match, instructions):
    return {
        "flow": [{
            "id": flow_id,
            "priority": priority,
            "table_id": table_id,
            "match": match,
            "instructions": instructions
        }]
    }
src_ip = None
if args.src_ip:
    src_ip = args.src_ip
in_port = None
if args.in_port:
    in_port = args.in_port
match = construct_match(src_ip, in_port)



flow = build_flow(args.flow_id, args.priority, args.table_id, match, instructions)
with open(f"flow_{args.flow_id}.json", "w") as f:
    json.dump(flow, f, indent=2)
print(f"Saved to flow_{args.flow_id}.json")