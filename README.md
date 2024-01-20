# amazon-bedrock-playground

learn [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide)

## demo

```sh
pipenv install

# login for boto3 credentials
aws sso login --profile root-AWSAdministratorAccess
```

- visit [`main.ipynb`](./main.ipynb)
- in vscode select `.venv` kernel in top right

---

run jupyter lab UI

```sh
pipenv run jupyter lab
# open http://localhost:8888/lab
```

## Concepts

### Foundation Models

### Knowledge base for Amazon Bedrock

- managed RAG
- create vector db

**Steps**

1. create data source (e.g. s3 bucket with pdf docs)
1. select embedding model (e.g. Amazon Titan G1 Embeddings - Text)
1. create and select a vector database (e.g. OpenSearch)
1. ingest data sources into knowledge base
1. test knowledge base - send queries and see the responses

### Agents

[Build a Foundation Model (FM) powered customer service bot with agents for Amazon Bedrock](https://github.com/aws-samples/amazon-bedrock-samples/tree/main/agents/agentsforbedrock-retailagent) - good example

**Steps**



**Action Groups** 

- tasks that the agent can perform autonomously
- Action groups are mapped to an AWS Lambda function and related API schema to perform API calls.

## resources

- <https://docs.aws.amazon.com/bedrock/latest/userguide>
- [aws-samples/amazon-bedrock-samples](https://github.com/aws-samples/amazon-bedrock-samples)
- [Build a Foundation Model (FM) powered customer service bot with agents for Amazon Bedrock](https://github.com/aws-samples/amazon-bedrock-samples/tree/main/agents/agentsforbedrock-retailagent)