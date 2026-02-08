import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Internship-Serverless-Table')

def lambda_handler(event, context):
    
    body = json.loads(event['body'])
    
    name = body.get('name')
    message = body.get('message')
    
    item = {
        'id': str(uuid.uuid4()),
        'name': name,
        'message': message
    }
    
    table.put_item(Item=item)
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps('Data stored successfully!')
    }
