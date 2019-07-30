#!/usr/bin/python

import boto3

#create a function to create an instance
def create_instance(bucketName):
    ec2 = boto3.resource('ec2')

    #Run a script to install the apache web server on the created instance
    user_script = """#!/bin/bash
           echo "Beginning to install apache" >> /tmp/log.txt
           sudo yum install httpd -y
           sudo systemctl enable httpd
           sudo service httpd start
           sudo yum install python3
           echo "<h2>Test page</h2> Instance ID: " >> /var/www/html/index.html
           curl --silent http://169.254.169.254/latest/meta-data/instance-id/ >> /var/www/html/index.html
           echo "<br>Availability zone:" >> /var/www/html/index.html
           curl --silent http://169.254.169.254/latest/meta-data/placement/availability-zone/ >> /var/www/html/index.html
           echo "<br>IP address: </td>" >> /var/www/html/index.html
           curl --silent http://169.254.169.254/latest/meta-data/public-ipv4 >> /var/www/html/index.html
           echo "<hr>Here is an image that I have stored on S3: <br>" >> /var/www/html/index.html
           echo "<img src=https://s3-eu-west-1.amazonaws.com/%s/image.jpg>" >> /var/www/html/index.html
           echo "Apache was installed" >> /tmp/log.txt""" % bucketName



    #Create an ec2 instance with my key and
    #security group WebServerSG and give the instance a tag name of Assignment One
    create_instance = ec2.create_instances(
        ImageId='ami-0bbc25e23a7640b9b',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName='MarieCloudAssignmentKey',
        UserData=user_script,
        SecurityGroups=[
            'WebServerSG',
        ],
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value':"Assignment One"
                    },
                ]
            }
        ]
    )
    print("Please wait while your ec2 instance is being started\n")
    create_instance[0].wait_until_running()
    create_instance[0].reload()
    print("Your instance was created with the id of " + create_instance[0].id)
    print(create_instance[0])



