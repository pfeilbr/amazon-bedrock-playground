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


## resources

- <https://docs.aws.amazon.com/bedrock/latest/userguide>
- [aws-samples/amazon-bedrock-samples](https://github.com/aws-samples/amazon-bedrock-samples)