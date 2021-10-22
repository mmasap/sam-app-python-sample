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
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET'
        },
        'body': json.dumps(result['Items']),
    }
