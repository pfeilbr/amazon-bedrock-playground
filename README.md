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

managed [Retrieval Augmented Generation (RAG)](https://www.promptingguide.ai/techniques/rag) 

**Steps**

1. create data source (e.g. s3 bucket with pdf docs)
2. select embedding model (e.g. Amazon Titan G1 Embeddings - Text)
3. create and select a vector database (e.g. OpenSearch)
4. ingest data sources into knowledge base
5. test knowledge base - send queries and see the responses

### Agents

[Build a Foundation Model (FM) powered customer service bot with agents for Amazon Bedrock](https://github.com/aws-samples/amazon-bedrock-samples/tree/main/agents/agentsforbedrock-retailagent) - good example

**Steps**



**Action Groups** 

- Action groups define the tasks that you want your agent to help customers carry out
- Action groups are mapped to an AWS Lambda function and related API schema to perform API calls.
- Knowledge bases provide a repository of information that the agent can query to answer customer queries and improve its generated responses.

- Action group consists of the following components that you set up
  - OpenAPI schema that define the APIs that your action group should call. Your agent uses the API schema to determine the fields it needs to elicit from the customer to populate for the API request.
  - A Lambda function that defines the business logic for the action that your agent will carry out.


## resources

- <https://docs.aws.amazon.com/bedrock/latest/userguide>
- [aws-samples/amazon-bedrock-samples](https://github.com/aws-samples/amazon-bedrock-samples)
- [Build a Foundation Model (FM) powered customer service bot with agents for Amazon Bedrock](https://github.com/aws-samples/amazon-bedrock-samples/tree/main/agents/agentsforbedrock-retailagent)