import json
import boto3
import os

def lambda_handler(event, context):
    
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
