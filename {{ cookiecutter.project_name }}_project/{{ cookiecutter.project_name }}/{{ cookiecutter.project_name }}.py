
def lambda_handler(event, context):
    squared_value = event['value']**2
    return {'squaredVal': squared_value}
