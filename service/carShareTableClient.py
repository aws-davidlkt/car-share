import boto3
import json
import logging
from collections import defaultdict

client = boto3.client('dynamodb')

#Retrieve all the cars from the table using Scan operation
def getAllCars():
    response = client.scan(
        TableName='Cars'
    )

    logging.info(response['Items'])

    carsList = defaultdict(list)
    for item in response['Items']:
        car = {}
        car['Id'] = item['Id']['S']
        car['Model'] = item['Model']['S']
        car['Plate'] = item['Plate']['S']
        car['Driver'] = item['Driver']['S']
        car['Distance'] = item['Distance']['N'],
        car['Reserved'] = item['Reserved']['BOOL'],
        car['Size'] = item['Size']['S'],
        car['Likes'] = item['Likes']['N'],
        car['Image'] = item['Image']['S'],
        car['DetailsImage'] = item['DetailsImage']['S']
        carsList['cars'].append(car)

    return json.dumps(carsList)

#Retrieve a car equal to the selected filter value using Query operation
def queryCars(queryParam):
    logging.info(json.dumps(queryParam))

    response = client.query(
        TableName='Cars',
        IndexName=queryParam['filter']+'Index',
        KeyConditions={
            queryParam['filter']: {
                'AttributeValueList': [
                    {
                        'S': queryParam['value']
                    }
                ],
                'ComparisonOperator': "EQ"
            }
        }
    )

    carsList = defaultdict(list)
    for item in response['Items']:
        car = {}
        car['Id'] = item['Id']['S']
        car['Model'] = item['Model']['S']
        car['Plate'] = item['Plate']['S']
        car['Driver'] = item['Driver']['S']
        car['Distance'] = item['Distance']['N'],
        car['Reserved'] = item['Reserved']['BOOL'],
        car['Size'] = item['Size']['S'],
        car['Likes'] = item['Likes']['N'],
        car['Image'] = item['Image']['S'],
        car['DetailsImage'] = item['DetailsImage']['S']
        carsList['cars'].append(car)

    return json.dumps(carsList)

#Retrieve a specific car using its unique key using GetItem operation
def getCar(Id):
    response = client.get_item(
        TableName='Cars',
        Key={
            'Id': {
                'S': Id
            }
        }
    )

    item = response['Item']

    car = {}
    car['Id'] = item['Id']['S']
    car['Model'] = item['Model']['S']
    car['Plate'] = item['Plate']['S']
    car['Driver'] = item['Driver']['S']
    car['Distance'] = item['Distance']['N'],
    car['Reserved'] = item['Reserved']['BOOL'],
    car['Size'] = item['Size']['S'],
    car['Likes'] = item['Likes']['N'],
    car['Image'] = item['Image']['S'],
    car['DetailsImage'] = item['DetailsImage']['S']

    return json.dumps(car)

# increment the number of likes for a car by 1
def likeCar(Id):

    # Use the DynamoDB API UpdateItem to increment the number of Likes
    # the car has by 1 using an UpdateExpression.
    response = client.update_item(
        TableName='Cars',
        Key={
            'Id': {
                'S': Id
            }
        },
        UpdateExpression="SET Likes = Likes + :n",
        ExpressionAttributeValues={':n': {'N': '1'}}
    )

    response = {}
    response["Update"] = "Success";

    return json.dumps(response)

# mark a car as reserved
def reserveCar(Id):

    # Use the DynamoDB API UpdateItem to set the value of the car's
    # Reserved attribute to True using an UpdateExpression.
    response = client.update_item(
        TableName='Cars',
        Key={
            'Id': {
                'S': Id
            }
        },
        UpdateExpression="SET Reserved = :b",
        ExpressionAttributeValues={':b': {'BOOL': True}}
    )

    response = {}
    response["Update"] = "Success";

    return json.dumps(response)
