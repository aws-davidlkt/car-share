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
        car['id'] = item['id']['S']
        car['Model'] = item['Model']['S']
        car['carPlate'] = item['carPlate']['S']
        car['driver'] = item['driver']['S']
        car['distanceKms'] = item['distanceKms']['N']
        carsList['cars'].append(car)

    return json.dumps(carsList)

#Retrieve a specific car using its unique key using GetItem operation
def getCar(id):
    response = client.get_item(
        TableName='Cars',
        Key={
            'id': {
                'S': id
            }
        }
    )

    item = response['Item']

    car = {}
    car['id'] = item['id']['S']
    car['Model'] = item['Model']['S']
    car['carPlate'] = item['carPlate']['S']
    car['driver'] = item['driver']['S']
    car['distanceKms'] = item['distanceKms']['N']
    car['Reserved'] = item['Reserved']['BOOL']

    return json.dumps(mysfit)