import yaml

def load_config(path="config.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)

config = load_config()

#ODL
ODL_HOST = config["odl"]["host"]
ODL_PORT = config["odl"]["port"]
ODL_USER = config["odl"]["username"]
ODL_PASSWORD = config["odl"]["password"]

#Controller
CONTROLLER_PORT = config["controller"]["port"]
RETRY_INTERVAL = config["controller"]["retry_interval"]
MAX_RETRIES = config["controller"]["max_retries"]
