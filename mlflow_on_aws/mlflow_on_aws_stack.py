from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as s3,
    RemovalPolicy,
    # aws_sqs as sqs,
)

from constructs import Construct


class MlflowOnAwsStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create an S3 bucket for MLflow artifacts
        s3_bucket = s3.Bucket(
            self,
            "MLFlowS3Bucket",
            bucket_name="<YOUR_S3_BUCKET>",
            removal_policy=RemovalPolicy.DESTROY,
        )
