import boto3
import pprint
import json

pp = pprint.PrettyPrinter(indent=4)

client = boto3.client('bedrock')

response = client.list_foundation_models()
pp.pprint(response)

prompt  = 'list three names of people'
bedrock_runtime_client = boto3.client('bedrock-runtime')
body = json.dumps(
                {
                    "prompt": prompt,
                    "maxTokens": 500,
                    "temperature": 0,
                    "stopSequences": [],
                })
res = bedrock_runtime_client.invoke_model(modelId='ai21.j2-ultra', body=body)
response_body = json.loads(res.get("body").read())
pp.pprint(response_body)
