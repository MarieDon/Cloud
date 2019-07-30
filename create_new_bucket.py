#!/usr/bin/env python3

import boto3

s3_bucket = boto3.resource('s3')

def put_file_in_bucket(bucket_name):
    file = "image.jpg"
    try:
        upload_file = s3_bucket.Object(bucket_name, file).put(ACL='public-read', ContentType='image/jpeg', Body=open(file, 'rb'))
        print("File was upload to " + bucket_name)
    except Exception as error:
        print("something went wrong and we could not up load you image to the bucket " + error)
