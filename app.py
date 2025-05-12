import json
import boto3
import os

def lambda_handler(event, context):
    
    event = json.loads(event['Records'][0]['body'])
    print(event, type(event))
    try:        
        return json.dumps({
            'statusCode':200,
            'key_phrases': 'test'})

    except Exception as e:
        print(e)
        print("Something went wrong.")
        return {
            'statusCode':404,
            'key_phrases': e}
