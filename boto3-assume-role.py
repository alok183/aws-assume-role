###############################################################################
# Author : Alok.Shrivastava
###############################################################################

import boto3
from boto3.session import Session
import os
def get_session(region, access_id, secret_key):
    return boto3.session.Session(region_name=region,
                                aws_access_key_id=access_id,
                                aws_secret_access_key=secret_key)
def assume_role(arn, session_name):
    """aws sts assume-role --role-arn arn:aws:iam::00000000000000:role/example-role --role-session-name example-role"""
    client = boto3.client('sts')
    account_id = client.get_caller_identity()["Account"]
    print(account_id)
    
    response = client.assume_role(RoleArn=arn, RoleSessionName=session_name)
    print(response)     
    session = Session(aws_access_key_id=response['Credentials']['AccessKeyId'],
                      aws_secret_access_key=response['Credentials']['SecretAccessKey'],
                      aws_session_token=response['Credentials']['SessionToken'])
    
    client = session.client('sts')
    account_id = client.get_caller_identity()["Account"]
    print(account_id)
    return session

# secret_key and access_key of the user created for assumerole
os.environ['AWS_SECRET_ACCESS_KEY']="<secret_key>"
os.environ['REGION']="us-east-2"
os.environ['AWS_ACCESS_KEY_ID']="<access_key>"
# os.unsetenv('REGION')
# usage:
session = assume_role('<arn_value_of_role_need_to_be_assumed_by_user>','alok')
# e.g.
#session = assume_role('arn:aws:iam::18443:role/assume-aal-rds-role','alok')
#client = session.client('rds',region_name='us-east-2')
#response = client.describe_db_clusters(DBClusterIdentifier='alok-test-db')
#print(response)
