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

Download boto3 for ColdStart and WarmStart scripts:
  ```sh
  pip install boto3

