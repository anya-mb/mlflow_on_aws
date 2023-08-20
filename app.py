#!/usr/bin/env python3
import os

import aws_cdk as cdk

from mlflow_on_aws.mlflow_on_aws_stack import MlflowOnAwsStack


app = cdk.App()
MlflowOnAwsStack(app, "MlflowOnAwsStack")

app.synth()
