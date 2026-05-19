import json

print("flow_id: ")
ID = input()
print("priority: ")
priority = input()

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