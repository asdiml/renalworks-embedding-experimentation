import boto3
import json

class BedrockCaller:

    def __init__(self) -> None:
        """
        Starts the boto3 session
        Important: Ensure that your AWS SSO credentials are configured. This can be done with `aws configure sso`. 
        """
        session = boto3.Session(profile_name='renalworks-bedrock') # Replace the profile name (can be found for Windows users in /Users/{YOUR_USERNAME}/.aws/config) accordingly 
        self.boto3_bedrock = session.client('bedrock-runtime')

    # Define function that obtains embedding from one of Bedrock's embedding models
    def get_embedding(self, text):

        body = json.dumps({"inputText": text})
        modelId = "amazon.titan-embed-text-v2:0"  # (Change this to try different embedding models)
        accept = "application/json"
        contentType = "application/json"

        response = self.boto3_bedrock.invoke_model(
            body=body, modelId=modelId, accept=accept, contentType=contentType
        )
        response_body = json.loads(response.get("body").read())

        embedding = response_body.get("embedding")
        return embedding

    def call_claude3sonnet(self, messages_API_body):

        body = json.dumps(messages_API_body)
        modelId = "anthropic.claude-3-sonnet-20240229-v1:0"  # (Change this to try different model versions)
        accept = "application/json"
        contentType = "application/json"

        response = self.boto3_bedrock.invoke_model(
            body=body, modelId=modelId, accept=accept, contentType=contentType
        )
        response_body = json.loads(response.get("body").read())
        return response_body