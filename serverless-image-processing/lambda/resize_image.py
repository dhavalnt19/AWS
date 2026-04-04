import json
import boto3
import os
from PIL import Image
import io

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

TABLE_NAME = os.environ.get("TABLE_NAME")
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    print("Event:", event)

    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']

        print(f"Processing file {key} from bucket {bucket}")

        response = s3.get_object(Bucket=bucket, Key=key)
        image_content = response['Body'].read()

        image = Image.open(io.BytesIO(image_content))

        # Resize image
        image.thumbnail((200, 200))

        buffer = io.BytesIO()
        image.save(buffer, "JPEG")
        buffer.seek(0)

        resized_key = f"resized-{key}"

        # Upload resized image
        s3.put_object(
            Bucket=bucket,
            Key=resized_key,
            Body=buffer,
            ContentType='image/jpeg'
        )

        # Store metadata in DynamoDB
        table.put_item(
            Item={
                "image_name": key,
                "resized_image": resized_key
            }
        )

    return {
        'statusCode': 200,
        'body': json.dumps('Image processed successfully!')
    }
