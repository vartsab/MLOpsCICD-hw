import json
from datetime import datetime


def lambda_handler(event, context):
    print("Logging metrics...")
    print(f"Received event: {json.dumps(event)}")

    result = {
        "status": "metrics_logged",
        "message": "Metrics were logged successfully",
        "input_from_previous_step": event,
        "logged_at": datetime.utcnow().isoformat() + "Z"
    }

    print(f"Metrics result: {json.dumps(result)}")
    return result
