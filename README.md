# AWS-Benchmark-Tests

# Lambda Test README

## Overview

This README provides instructions to perform Cold Start and Warm Start tests on AWS Lambda functions using boto3. Each test will execute the specified Lambda function 100 times. Additionally, instructions for concurrent invocation of a Lambda function are provided.

## Prerequisites

Ensure Python and pip are installed on your system:

- **Python Installation**: Download Python from the [Official Python Website](https://www.python.org/downloads/).
- If pip is missing, follow the instructions on the Pip Installation Guide.


- **Verify Pip Installation**: Pip comes installed with Python. Verify its presence by running:
  ```sh
  pip --version
  
## Steps to Perform Cold Start Test

1. **Change the Lambda Function Name**:
   - Open the file `measure.py`.
   - Locate the variable `LAMBDA_FUNCTION_NAME` and change its value to your actual Lambda function name.

     ```python
     LAMBDA_FUNCTION_NAME = 'your_lambda_function_name'  # Replace with your actual Lambda function name

2. **Run the Script**:
   - Execute the script using the following command:
   ```sh
   python measure.py

## Steps to Perform Warm Start Test

1. **Modify the Script**:
   - Open the file `warmstart.py`.
   - Find the variable `LAMBDA_FUNCTION_NAME` in the script and change its value to your actual Lambda function name.

     Example snippet from `warmstart.py`:
     ```python
     LAMBDA_FUNCTION_NAME = 'your_lambda_function_name'  # Replace with your actual Lambda function name


## Steps to Perform Concurrent Start Test
### Installing the required modules

Change the directory to root module and then please run the below command.

```
pip install -r requirements.txt
```

### Running the code 
In the below give function arn and no of concurrent users and duration it need to be called it will infinitely call till that duration
```
python invoke_concurrently.py --function_arn arn:aws:lambda:region:account-id:function:function-name --concurrent_users 10 --duration 60
```
To save to CSV file 

```
python invoke_concurrently.py --function_arn arn:aws:lambda:region:account-id:function:function-name --concurrent_users 10 --duration 60 --output_file output.csv
```

Download boto3 for ColdStart and WarmStart scripts:

  ```sh
  pip install boto3
