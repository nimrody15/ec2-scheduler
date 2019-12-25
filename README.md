# Overview ec2-scheduler

EC2 Scheduler is a project that will help you manage your EC2 Instances power on/off policy.

Deploy the Cloudformation in a region of your choice.

Tag the instances you want to manage and the scheduler will do the rest.

Example for tags:

TagName: PowerOn  
Tag Value: 09:00

TagName: PowerOff  
Tag Value: 18:00


## End Of Day Shut Down

1. If you want to shut down all instances at the end of each day, choose end of day parameter to 'Yes'

2. Insert the time want to shut down the instances (GMT).

**Important** Once you choose 'Yes' - ALL INSTANCES WILL BE SHUT DOWN AT THAT SPECIFIC TIME.

3. If you want to keep instances and ignore end of day shut down,add the below tag:

TagName: KeepAlive  
Tag Value: true


How To Use The Solution
------------------------
Automatically: <a href="https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=myteststack&templateURL=https://pas-on-cloud.s3.eu-west-2.amazonaws.com/ec2-scheduler.json" target="_blank"><img src="https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png"/></a>

Manually: 

* Clone the solution to your computer

* Deploy the cloudformation using S3 uplod/ CLI/ Designer...
  For Example: Copy the content of the file ec2-scheduler.json and deploy it in Cloudformation Designer
![step1](https://i.postimg.cc/fTRGKZfR/cfn1.png "Step1")

* Give the Cloudformation Stack a name, set the desired Lambda intervals (default 15 minutes)
* Optional - Choose End of day to shut down all untagged instances
![step2](https://i.postimg.cc/FKxWCqPK/ec2-scheduler.png "Step2")

* Tag your instances
![step3](https://i.postimg.cc/13gbkHTx/cfn3.png "Step3")


Author Information
------------------
For questions, support and issues, contact Nimrod Yakobovitz, Nimrod.Yakobovitz@Cyberark.com
