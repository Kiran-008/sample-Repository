import boto3

def uploading_file(name,path):

    s3 = boto3.client("s3",
                  region_name='us-east-1',
                  aws_access_key_id='AKIAYTTPC3LC6BIO6HVJ',
                  aws_secret_access_key='ZhZV+fmWAlpeNKWA+iW/a2nZcuGxuZcabLTjkzwe')

    response = s3.list_objects(Bucket=name)

    s3.upload_file(Filename=path, Bucket=name, Key='sample/sample.pdf')
    print(response)
name=input("Enter the Bucket Name")
path=input("Enter the File path that you want to upload")
uploading_file(name,path)