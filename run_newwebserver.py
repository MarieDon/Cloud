import datetime
import time
from create_new_instance import create_instance
from create_new_bucket import put_file_in_bucket
from create_bucket import createBucket

def main():
    user_choice = ""
    correct_bucket_name = False
    bucket = input("Please enter a name for your bucket ")
    bucket = bucket.lower()
    while not correct_bucket_name:
        user_choice = input("Are you sure this is the correct name for your bucket Y/N ")
        if user_choice == "Y":
            correct_bucket_name = True
        else:
           bucket = input("Please enter a name for your bucket ")


    secs = datetime.datetime.now()
    bucket_name = bucket + str(secs.microsecond)

    createBucket(bucket_name)
    put_file_in_bucket(bucket_name)
    create_instance(bucket_name)

if __name__ == '__main__':
    main()
