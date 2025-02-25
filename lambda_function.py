import json

def lambda_handler(event, context):
    #dump de input voor troubleshooting
    varq=json.dumps(event, indent=2)

    # Extract the two arguments from the event
    arg1 = event.get('arg1')
    arg2 = event.get('arg2')
    ret1 =""
    if arg1 == "eerste":
      ret1 = "tien"
    else:
      ret1 = "twintig"
        
    # Perform some operation with the arguments
    result = f"Received arg1: {arg1}, arg2: {arg2}, return1: {ret1}"
        
    # Return the result
    return {
            'statusCode': 200,
            'body': json.dumps(result),
            'testje': varq
    }

