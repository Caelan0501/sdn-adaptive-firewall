import requests
from requests.auth import HTTPBasicAuth
import json

ODL = "http://127.0.0.1:8181/rests/data"
AUTH = HTTPBasicAuth('admin', 'admin')

def install_flow(node_id, flow_id="1"):
    url = f"{ODL}/flow-node-inventory:nodes/node={node_id}/table=0/flow={flow_id}"

    flow = {
        "flow": [{
            "id": flow_id,
            "priority": 500,
            "table_id": 0,
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

    headers = {"Content-Type": "application/json"}
    r = requests.put(url, auth=AUTH, data=json.dumps(flow), headers=headers)

    print("Status:", r.status_code)
    print(r.text)

if __name__ == '__main__':
    install_flow("openflow:1")