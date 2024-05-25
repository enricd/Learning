from boto3 import resource
from boto3.dynamodb.conditions import Attr, Key
from datetime import datetime


demo_table = resource("dynamodb").Table("demo-dynamo-python")


def insert():
    print("demo insert")

    response = demo_table.put_item(
        Item={
            "customer_id": "cus-05",    # Partition key
            "order_id": "ord-8",       # Sort key
            "status": "pending",
            "order_date": datetime.now().isoformat()
        }
    )
    print(f"Insert response: {response}")


def select_scan():
    print("demo select scan")
    filter_expression = Attr("status").eq("pending")
    
    item_list = []
    dynamo_response = {"LastEvaluatedKey": False}   # used for pagination
    while "LastEvaluatedKey" in dynamo_response:
        if dynamo_response["LastEvaluatedKey"]:
            dynamo_response = demo_table.scan(
                FilterExpression=filter_expression,
                ExclusiveStartKey=dynamo_response["LastEvaluatedKey"]
            )
            print(f"response-if: {dynamo_response}")

        else:
            dynamo_response = demo_table.scan(
                FilterExpression=filter_expression
            )
            print(f"response-else: {dynamo_response}")

        for i in dynamo_response["Items"]:
            item_list.append(i)

    print(f"\nNumber of input tasks to process: {len(item_list)}")
    for item in item_list:
        print(f"Item: {item}")


def query_by_partition_key(cutomer_value):
    print("demo query by partition key")

    response = {}
    filtering_exp = Key("customer_id").eq(cutomer_value)
    response = demo_table.query(
        KeyConditionExpression=filtering_exp
    )
    # print(f"Query response: {response}")
    # print(f"Items: {response['Items']}")

    for item in response["Items"]:
        print(f"Item: {item}")


def query_by_partition_key_order(customer_value):
    print("demo query by partition key and sort key")

    response = {}
    filtering_exp = Key("customer_id").eq(customer_value)
    response = demo_table.query(
        KeyConditionExpression=filtering_exp,
        ScanIndexForward=True,
    )
    # print(f"Query response: {response}")
    # print(f"Items: {response['Items']}")

    for item in response["Items"]:
        print(f"Item: {item}")


# create a new global index on status first
def query_by_index_key(status_value):
    print("demo query by index key")

    filtering_exp = Key("status").eq(status_value)
    response = demo_table.query(
        IndexName="status-index",
        KeyConditionExpression=filtering_exp,
        ScanIndexForward=False,
    )

    for item in response["Items"]:
        print(f"Item: {item}")


def query_by_partition_key_and_sort_key(customer_value, order_value):
    print("demo query by partition key and sort key")

    response = {}
    filtering_exp1 = Key("customer_id").eq(customer_value)
    filtering_exp2 = Key("order_id").eq(order_value)
    response = demo_table.query(
        KeyConditionExpression=filtering_exp1 & filtering_exp2
    )

    for item in response["Items"]:
        print(f"Item: {item}")


def update(customer_value, status_value):
    print("demo update")
    response = demo_table.update_item(
        Key={
            "customer_id": customer_value,

        },
        UpdateExpression="set status=:r, updated_date:d",
        ExpressionAttributeValues={
            ":r": status_value,
            ":d": datetime.now().isoformat()
        },
        ReturnValues="UPDATED_NEW"
    )


def update_with_expression_name(customer_value, status_value):
    print("demo update with expression name")
    response = demo_table.update_item(
        Key = {
            "customer_id": customer_value,
            "order_id": "ord-1"

        },
        UpdateExpression="set #status=:r, updated_date=:d",
        ExpressionAttributeValues={
            ":r": status_value,
            ":d": datetime.now().isoformat()
        },
        ExpressionAttributeNames={
            "#status": "status"
        },
        ReturnValues="UPDATED_NEW"
    )
    print(f"Update response: {response}")


def batch_delete_transaction_records(items_to_delete):
    print("demo delete")
    response = {}
    # deletes everything in a single query (request) rather than one by one
    with demo_table.batch_writer() as batch:
        for item in items_to_delete:
            response = batch.delete_item(
                Key={
                    "customer_id": item["customer_id"],
                    "order_id": item["order_id"]
                }
            )
            print(f"Delete response: {response}")


if __name__ == "__main__":
    insert()
    # select_scan()
    # query_by_partition_key("cus-01")
    # query_by_partition_key_order("cus-01")
    # query_by_index_key("completed")
    # query_by_partition_key_and_sort_key("cus-01", "ord-1")
    # update("cus-01", "completed")
    # update_with_expression_name("cus-01", "completed")

    items = [
        {"customer_id": "cus-04", "order_id": "ord-6"},
        {"customer_id": "cus-05", "order_id": "ord-8"}
    ]

    batch_delete_transaction_records(items)