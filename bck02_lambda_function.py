import json
import boto3
#pip install boto3


'''  gebruik dynamodb
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('your-table-name')
    
    response = table.get_item(Key={'your-primary-key': 'your-key-value'})
    item = response.get('Item')
    
    return item

'''
def lambda_handler(event, context):
    #dump de input voor troubleshooting
    varq=json.dumps(event, indent=2)
   
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('users')

    mykeyvalue=event.get('arg1')
    response = table.get_item(Key={'email': mykeyvalue})
    ret1 = response.get('voornaam')
   # return item

    
    # Extract the two arguments from the event
    arg1 = event.get('arg1')
    arg2 = event.get('arg2')
    
    ''' ret1 =""
    if arg1 == "eerste":
      ret1 = "tien"
    else:
      ret1 = "twintig"
    '''  

    # Perform some operation with the arguments
    result = f"Received arg1: {arg1}, arg2: {arg2}, return1: {ret1}"
        
    # Return the result
    return {
            'statusCode': 200,
            'body': json.dumps(result),
            'testje': varq
    }

