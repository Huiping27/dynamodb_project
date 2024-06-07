
import boto3

# Initialize a session using Amazon DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

# Create DynamoDB table
def create_table():
    table = dynamodb.create_table(
        TableName='Users',
        KeySchema=[
            {
                'AttributeName': 'username',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'username',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    print("Table status:", table.table_status)

# Add a user to the Users table
def add_user(username, first_name, last_name):
    table = dynamodb.Table('Users')
    table.put_item(
        Item={
            'username': username,
            'first_name': first_name,
            'last_name': last_name
        }
    )
    print(f"Added user: {username}")

# Get user details
def get_user(username):
    table = dynamodb.Table('Users')
    response = table.get_item(
        Key={
            'username': username
        }
    )
    item = response.get('Item')
    print(item)

# Update user details
def update_user(username, first_name, last_name):
    table = dynamodb.Table('Users')
    table.update_item(
        Key={
            'username': username
        },
        UpdateExpression='SET first_name = :f, last_name = :l',
        ExpressionAttributeValues={
            ':f': first_name,
            ':l': last_name
        }
    )
    print(f"Updated user: {username}")

# Delete user
def delete_user(username):
    table = dynamodb.Table('Users')
    table.delete_item(
        Key={
            'username': username
        }
    )
    print(f"Deleted user: {username}")

if __name__ == "__main__":
    create_table()
    add_user('jdoe', 'John', 'Doe')
    get_user('jdoe')
    update_user('jdoe', 'Johnny', 'Doe')
    get_user('jdoe')
    delete_user('jdoe')
