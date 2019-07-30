import boto3
ec2 = boto3.resource('ec2')

for inst in ec2.instances.all():
    print (inst.id)
