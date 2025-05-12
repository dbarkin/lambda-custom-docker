import json
import boto3
import os
import subprocess
import shutil

def lambda_handler(event, context):
    # Copy the script to /tmp directory
    # Set the executable permission to the script
    # Run the script
    result = subprocess.run(["atlas", "--version"], capture_output=True, text=True)
    return {
        'statusCode': 200,
        'body': result.stdout
    }
