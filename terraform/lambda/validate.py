import json
from datetime import datetime


def lambda_handler(event, context):
    print("Validating data...")
    print(f"Received event: {json.dumps(event)}")

    source = event.get("source", "unknown")
    commit = event.get("commit", "unknown")

    result = {
        "status": "validated",
        "message": "Data validation completed successfully",
        "source": source,
        "commit": commit,
        "validated_at": datetime.utcnow().isoformat() + "Z"
    }

    print(f"Validation result: {json.dumps(result)}")
    return result
