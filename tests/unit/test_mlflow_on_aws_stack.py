import aws_cdk as core
import aws_cdk.assertions as assertions

from mlflow_on_aws.mlflow_on_aws_stack import MlflowOnAwsStack


# example tests. To run these tests, uncomment this file along with the example
# resource in mlflow_on_aws/mlflow_on_aws_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = MlflowOnAwsStack(app, "mlflow-on-aws")
    template = assertions.Template.from_stack(stack)


#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
