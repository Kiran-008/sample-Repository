import boto3
import os
name= 'my-bucket89843'
s3 = boto3.client("s3",
                  region_name='us-east-1',
                  aws_access_key_id='AKIA3TLHNXYINOO667GX',
                  aws_secret_access_key='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')
response = s3.list_objects(Bucket=name)
print(response)
# cmd = 'aws s3 sync s3://my-bucket89843/ python_practice'
res=os.system('aws s3 sync . s3://my-bucket89843')
res1=os.system('aws s3 sync C:/Users/Kiran_Bommapala/Documents/intro-to-CloudFormation_AC-master s3://my-bucket89843')


