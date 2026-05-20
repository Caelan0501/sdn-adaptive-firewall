import argparse
import json

def construct_match(src_ip=None, in_port=None):
    match = {}
    if src_ip is not None:
        match["ip-match"] = {}
        match["ipv4-source"] = src_ip
    if in_port is not None:
        match["in-port"] = in_port
    return match

def construct_actions(action):
    actions = []
    if action == "NORMAL":
        actions.append({
            "order": 0,
            "output-action": {
                "output-node-connector": "NORMAL"
            }
        })
    elif action == "DROP":
        actions.append({
            "order": 0,
            "drop-action": {}
        })
    elif action and action.startswith("output:"):
        port = action.split(":")[1]
        actions.append({
            "order": 0,
            "output-action": {
                "output-node-connector": port
            }
        })
    return actions

def construct_instructions(actions):
    instructions = {
        "instruction": [{
            "order": 0,
            "apply-actions": {
                "action": actions
            }
        }]
    }
    return instructions

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

def save_flow(flow_id, flow):
    with open(f"flow_{flow_id}.json", "w") as f:
        json.dump(flow, f, indent=2)
    print(f"Saved to flow_{args.flow_id}.json")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate ODL flow rules")
    parser.add_argument("--flow-id", required=True)
    parser.add_argument("--priority", type=int, default=500)
    parser.add_argument("--table-id", type=int, default=0)
    parser.add_argument("--src_ip")
    parser.add_argument("--in_port")
    parser.add_argument("--action", default="NORMAL", help="NORMAL, DROP, or output:<port>")
    args = parser.parse_args()

    match = construct_match(args.src_ip, args.in_port)
    actions = construct_actions(args.action)
    instructions = construct_instructions(actions)

    flow = build_flow(args.flow_id, args.priority, args.table_id, match, instructions)
    save_flow(args.flow_id, flow)