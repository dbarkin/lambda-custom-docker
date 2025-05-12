import json
import boto3
import subprocess

def lambda_handler(event, context):
    # Copy the script to /tmp directory
    # Set the executable permission to the script
    # Run the script
    #result = subprocess.run(["python", "-c", "import time; time.sleep(1)"], capture_output=True, text=True, check=True)
    #print('output: ', result.stdout)
    #print('error: ', result.stderr)
    result = subprocess.run(["/usr/bin/atlas", "--version"], capture_output=True, text=True, check=True)
    print('output: ', result.stdout)
    print('error: ', result.stderr)
    
    return {
        'statusCode': 200,
        'body': result.stdout
    }
