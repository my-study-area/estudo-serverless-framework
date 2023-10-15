# import json


# import json
# import boto3

def hello(event, context):
    # s3 = boto3.client('s3', endpoint_url="http://0.0.0.0:4566")
    # buckets = s3.list_buckets()
    # buckets_names = [bucket.get('Name') for bucket in buckets['Buckets']]
    # response = {"buckets": buckets_names}
    # return {
    #     "statusCode": 200,
    #     "body": json.dumps(response),
    #     "event": json.dumps(event)
    # }
    return {
        "statusCode": 200,
        "body": "Olá, mundo!"
    }


if __name__ == "__main__":
    hello(None, None)
    print("rodouuuu")
