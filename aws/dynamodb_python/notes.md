# LoveToCode YouTube channel: DynamoDB with Python

- Go to AWS and create a new DynamoDB table
- Name: demo-dynamo-python
- Primary key: customer_id (String)
- Sort key: order_id (Number)

- pip install boto3
- set index.py with code logic to load an item

- Install the aws cli and then create a new IAM user with programmatic access and the access key and secret key
- aws configure
- aws configure --profile myprofile
- aws configure list

- develop insert(), select_scan(), query_by_partition_key(), query_by_partition_key_order()

- create a global index in aws 

- develop query_by_global_index(), query_by_partition_key_and_order_key(), def batch_delete_transaction_records()
