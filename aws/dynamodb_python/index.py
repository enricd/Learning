from boto3 import resource
from boto3.dynamodb.conditions import Attr, Key
from datetime import datetime


demo_table = resource("dynamodb").Table("demo-dynamo-python")

def insert():
    print("demo insert")

    response = demo_table.put_item(
        Item={
            "customer_id": "cus-02",    # Partition key
            "order_id": "ord-3",       # Sort key
            "status": "pending",
            "order_date": datetime.now().isoformat()
        }
    )
    print(f"Insert response: {response}")


insert