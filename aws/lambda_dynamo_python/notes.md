# AWS Lambda with DynamoDB tutorial from pixegami

- go to aws console and create a new lambda function with Python and default settings
- define a test event with a json payload
- define the code logic in the lambda function from vscode
- create a dynamodb table from aws console

- configure execution role for the lambda function to access the dynamodb table, under Lambda > Configuration > Permissions > Execution role > the execution role of that lambda needs to have the policy to access the dynamodb table > Add permission > Attach policies > AmazonDynamoDBFullAccess