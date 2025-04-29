import json
import boto3
import os

# env variables for aws client
S3_BUCKET = os.getenv('S3_BUCKET')
S3_KEY = os.getenv('S3_KEY')
S3_SECRET = os.getenv('S3_SECRET')
S3_REGION = 'ca-central-1'

s3 = boto3.client(
    "s3", 
    aws_access_key_id=S3_KEY,
    aws_secret_access_key=S3_SECRET, 
    region_name = S3_REGION)

def handler(event, context):
    
    event = json.loads(event['body'])
    print(event, type(event))
    try: 
        txt = event['title'] + event['abstract']
        return json.dumps({
            'statusCode':200,
            'key_phrases': 'test'})

    except Exception as e:
        print(e)
        print("Something went wrong. Can't get abstract and title")
        return {
            'statusCode':404,
            'key_phrases': e}
