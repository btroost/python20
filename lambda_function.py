import json
import boto3
#*** script 20.a
#pip install boto3

def lambda_handler(event, context):
    #dump de input voor troubleshooting
    varq=json.dumps(event, indent=2)
   
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('users')

    mykeyvalue=event.get('arg1')
    #mykeyvalue="abcd@xyz.com" # for testing
    ret2="kokokok"
    try:
      response = table.get_item(Key={'email': mykeyvalue})
      ret1 = response.get('Item')
      if not ret1 == None:
        try:
          ret2 = ret1['voornaam']
        except:
          ret2 = "veld niet gevonden"
      else:
        ret2 = "record niet gevonden" 
    except:
      ret2 = "error in db request"
    
    # Extract the two arguments from the event
    arg1 = event.get('arg1')
    arg2 = event.get('arg2')
    
    # Perform some operation with the arguments
    result = f"Received arg1: {arg1}, arg2: {arg2}, return1: {ret2}"
        
    # Return the result
    return {
            'statusCode': 200,
            'body': json.dumps(result),
            'testje': varq
    }

