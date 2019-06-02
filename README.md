# Overview ec2-scheduler

EC2 Scheduler is a project that will help you manage your EC2 Instances power on/off policy.

Deploy the Cloudformation is a region of your choice.

Tag the instances you want to manage and the scheduler will do the rest.

Example for tags:

TagName: PowerOn  
Tag Value: 18:00

TagName: PowerOff  
Tag Value: 09:00

**That's it, you'r all set!** Instances will be powered on and off according to your tags

** NOTE ** The solution affecting only Instances With PowerOff/PowerOn tags, Instances without these tags are not affected

** Optional ** If ypu want all untagged Instances to power off (not related to PowerOff tag) every day at specific time, insert the time you want the Instances to be shut down and a Lambda will do the rest.
If you want to keep instances on add the below tag:

TagName: KeepAlive  
Tag Value: true

How To Use The Solution
------------------------

* Clone the solution to your computer

* Deploy the cloudformation using S3 uplod/ CLI/ Designer...
  For Example: Copy the content of the file ec2-scheduler.json and deploy it in Cloudformation Designer
![step1](https://i.postimg.cc/fTRGKZfR/cfn1.png "Step1")

* Give the Cloudformation Stack a name, set the desired Lambda intervals (default 15 minutes)
* Optional - Enter time for End of day Event to shut down all untagged instances
![step2](https://i.postimg.cc/022wvm0z/ec2-scheduler.png "Step2")

* Tag your instances
![step3](https://i.postimg.cc/13gbkHTx/cfn3.png "Step3")


Author Information
------------------
For questions, support and issues, contact Nimrod Yakobovitz, Nimrod.Yakobovitz@Cyberark.com
