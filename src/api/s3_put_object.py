import json
import os
import boto3
import botostubs
import datetime

s3: botostubs.S3.S3Resource = boto3.resource('s3')
bucket = s3.Bucket(os.environ['BUCKET_NAME'])


def lambda_handler(event, context):

    file_name = datetime.datetime.today().strftime('%Y%m%d%H%M%S') + '.txt'

    bucket.put_object(
        Key=file_name,
        Body='content',
    )

    return {
        'statusCode': 200,
        'body': json.dumps({
            'file_name': file_name
        }),
    }
