import logging
import boto3
from botocore.exceptions import ClientError
#import json
import time
# taking the input from user where want to create internet gateway 
REGION= input("Please, Enter the region name where you want to Delete this NACL:-")
client = boto3.client("ec2", region_name=REGION)


# setup the logger config
logger_info = logging.getLogger()
logging.basicConfig(level=logging.INFO,format=' %(message)s')
# function to delete the internet gateway 
def delete_gateway(internet_gateway_id):

    try:
        response = client.delete_internet_gateway(
            InternetGatewayId=internet_gateway_id)

    except ClientError:
        logger_info.exception('Sorry, Not able to create the internet gateway in given VPC')
        raise
    else:
        return response


if __name__ == '__main__':

    # taking input from the user to get the input id from the user
    id= input("Please, Enter the internet gateway ID to delete that:- ")
    
    logger_info.info('Deleting an internet gateway...')
    for i in range(3):
        logger_info.info(f'Please wait ......  \n We are deleting your internet gateway...\U0001F570')
        time.sleep(3)    
    network_acl = delete_gateway(id)
    logger_info.info(f'\nHurry, Your Internet Gateway {id} has been  deleted successfully \U0001F44D ')