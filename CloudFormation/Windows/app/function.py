import json


def handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps(event, sort_keys=True, indent=2)
    }
