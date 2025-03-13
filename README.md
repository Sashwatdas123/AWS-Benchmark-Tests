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

Download boto3 for ColdStart and WarmStart scripts:

  ```sh
  pip install boto3
