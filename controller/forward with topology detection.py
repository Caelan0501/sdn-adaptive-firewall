import requests
from requests.auth import HTTPBasicAuth
import json

ODL = "http://127.0.0.1:8181/rests/data"
AUTH = HTTPBasicAuth('admin', 'admin')
HEADERS = {'Content-Type': 'application/json'}

def install_forward_flow(node_id, table_id="0", flow_id="1"):
    url = f"{ODL}/opendaylight-inventory:nodes/node={node_id}/flow-node-inventory:table={table_id}/flow-node-inventory:flow={flow_id}"
    flow = {
        "flow": [{
            "id": flow_id,
            "priority": 500,
            "table_id": table_id,
            "match": {},
            "instructions": {
                "instruction": [{
                    "order": 0,
                    "apply-actions": {
                        "action": [{
                            "order": 0,
                            "output-action": {
                                "output-node-connector": "NORMAL"
                            }
                        }]
                    }
                }]
            }
        }]
    }

    r = requests.put(url, auth=AUTH, data=json.dumps(flow), headers=HEADERS)
    print("Status:", r.status_code)
    print(r.text)

def install_all(topology):
    """Install a forward flow on every discovered switch."""
    print(f"\n[*] Installing flows on {len(topology)} switch(es)...")
    for node_id in topology:
        install_forward_flow(node_id, flow_id=f"forward-{node_id.replace(':', '-')}")

def get_topology():
    url = f"{ODL}/opendaylight-inventory:nodes?content=nonconfig"
    r = requests.get(url, auth=AUTH, headers=HEADERS)
    r.raise_for_status()

    topology = {}
    nodes = r.json().get("nodes, {}").get("node", [])
    for node in nodes:
        node_id = node["id"]
        # Skip non-OpenFlow nodes
        if not node_id.startswith("openflow:"):
            continue
        # Get ports, filter out LOCAL (control port)
        connectors = node.get("node-connector", [])
        ports = [
            c["id"] for c in connectors
            if not c["id"].endswith("LOCAL")
        ]
        topology[node_id] = sorted(ports)
    return topology

def print_topology(topology):
    """Pretty print the discovered topology."""
    print(f"\n[*] Discovered {len(topology)} switch(es):")
    for node_id, ports in topology.items():
        print(f"\n  Switch: {node_id}")
        for port in ports:
            # Extract just the port number for readability
            port_num = port.split(":")[-1]
            print(f"    └── Port {port_num}: {port}")

def get_nodes(topology):
    """Return just the list of switch IDs."""
    return list(topology.keys())

def get_ports(topology, node_id):
    """Return port IDs for a specific switch."""
    return topology.get(node_id, [])

def get_port_numbers(topology, node_id):
    """Return just the port numbers (not full connector IDs) for a switch."""
    return [p.split(":")[-1] for p in get_ports(topology, node_id)]

if __name__ == '__main__':
    topology = get_topology()
    print_topology(topology)
    install_all(topology)