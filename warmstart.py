import boto3
import time
import json

# Variables
LAMBDA_FUNCTION_NAME = '<Your Lambda Function Name>'
COUNTER = 0
REGION = 'us-east-1'
MAX_INVOCATIONS = 100
SLEEP_TIME_FOR_INVOCATION = 1

# Initialize boto3 clients
lambda_client = boto3.client('lambda', region_name=REGION)



# Function to invoke Lambda
def invoke_lambda(function_name, counter):
    payload = json.dumps({'counter': counter})
    
    response = lambda_client.invoke(
        FunctionName=function_name,
        InvocationType='RequestResponse',  # Synchronous invocation
        Payload=payload
    )
    
    print(f"Lambda invoked with counter {counter}")
    
    return response['Payload'].read()



# Main process
while COUNTER < MAX_INVOCATIONS:
    # Invoke the Lambda function
    invoke_lambda(LAMBDA_FUNCTION_NAME, COUNTER)
    
    
    
    # Increment the counter
    COUNTER += 1
    
    # Wait for 1 second before next iteration
    time.sleep(SLEEP_TIME_FOR_INVOCATION)

print(f"Process completed. Lambda function invoked {MAX_INVOCATIONS} times.")