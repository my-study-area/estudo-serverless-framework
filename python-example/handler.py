import json
import os


def hello(event, context):
    myenv = os.getenv('VAR1','default')
    body = {
        "message": f"Python running with serverless, my local VAR1 is {myenv}",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}
