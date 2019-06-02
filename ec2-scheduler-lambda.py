import os
import boto3
import json
from datetime import datetime
from datetime import timedelta

def lambda_handler(event, context):

    ec2Client = boto3.client('ec2')
    regions = [region['RegionName'] for region in ec2Client.describe_regions()['Regions']]
    #regions = ['eu-north-1']
    currentTime = datetime.now() + timedelta(hours=3)

    for regionName in regions:
        print('-------- Region:{0} ---------'.format(regionName))
        ec2Client = boto3.client('ec2', region_name=regionName)
        response = ec2Client.describe_instances(MaxResults=100)

        instancesToStop = []
        instancesToStart = []
        for reservations in response['Reservations']:
            instanceId = ''
            instanceName = ''
            state = ''
            retainInstance = False

            for instanceDetails in reservations['Instances']:
                instanceId = instanceDetails['InstanceId']

                # ignore spot and scheduled instances
                if 'InstanceLifecycle' in instanceDetails.keys():
                    continue

                state = instanceDetails['State']
                if 'Tags' in instanceDetails:
                    for tag in instanceDetails['Tags']:
                        if tag['Key'] == 'Name':
                            instanceName = tag['Value'] if tag['Value'] != '' else 'Instance with no name'

                        if tag['Key'] == 'PowerOff':
                            poweroffTag = tag['Value'].split(':')
                            poweroffTime = currentTime.replace(hour=int(poweroffTag[0]), minute=int(poweroffTag[1]))
                            if  (poweroffTime <= currentTime <= poweroffTime + timedelta(minutes=65)) and (state['Name'] == 'running'):
                                print('instance: {0}({1}) will be shut down'.format(instanceName,instanceId))
                                instancesToStop.append(instanceId)

                        if tag['Key'] == 'PowerOn':
                            poweronTag = tag['Value'].split(':')
                            poweronTime = currentTime.replace(hour=int(poweronTag[0]), minute=int(poweronTag[1]))
                            if  poweronTime <= currentTime <= (poweronTime + timedelta(minutes=
                             {
                                "Ref":"SchedulerMinutes"
                             },
                             )) and (state['Name'] == 'stopped'):
                                print('instance {0}({1}) will be shut down'.format(instanceName,instanceId))
                                instancesToStart.append(instanceId)

        if (len (instancesToStop) <= 0):
            print ('No Instances found to stop')
        else:
            res = ec2Client.stop_instances(
                InstanceIds = instancesToStop,
                DryRun = False
            )

        if (len (instancesToStart) <= 0):
            print ('No Instances found to start')
        else:
            res = ec2Client.start_instances(
                InstanceIds = instancesToStart,
                DryRun = False
            )


        print ('~~~~~~ Region {0} - Stopped {1} instnaces ~~~~~~'.format(regionName, len(instancesToStop)))
        print ('~~~~~~ Region {0} - Started {1} instnaces ~~~~~~'.format(regionName, len(instancesToStart)))