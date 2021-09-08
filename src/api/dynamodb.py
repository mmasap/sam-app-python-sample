import os
import boto3
import botostubs
import json

dynamodb: botostubs.DynamoDB.DynamodbResource = boto3.resource('dynamodb')
table_name = os.environ['TABLE_NAME']


def lambda_handler(event, context):
    result = dynamodb.Table(table_name).scan()
    return {
        'statusCode': 200,
        'body': json.dumps(result['Items']),
    }
