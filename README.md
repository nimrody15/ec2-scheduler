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

How To Use The Solution
------------------------

* Clone the solution to your computer
![step1](/ec2-scheduler/info/cfn1.jpg?raw=true "Step1")
* Deploy the cloudformation using S3 uplod/ CLI/ Designer...
  For Example: Copy the content of the file ec2-scheduler.json and deploy it in Cloudformation Designer
* Give the Cloudformation Stack a name, set the desired Lambda intervals (default 15 minutes)
* Tag your instances


Author Information
------------------
For questions, support and issues, contact Nimrod Yakobovitz, Nimrod.Yakobovitz@Cyberark.com
