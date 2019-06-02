import os
import boto3
import json
from datetime import datetime
from datetime import timedelta

def lambda_handler(event, context):

    ec2Client = boto3.client('ec2')
    regions = ['eu-north-1']
    print (regions)
    currentTime = datetime.now() + timedelta(hours=3)
    print (currentTime)

    for regionName in regions:
        print('~~~~~~Region:{0}~~~~~~'.format(regionName))
        ec2Client = boto3.client('ec2', region_name=regionName)
        response = ec2Client.describe_instances(MaxResults=100)
        print (response)

        instancesToStop = []
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

                        if tag['Key'] == 'KeepAlive':
                            isKeepAlive = True if tag['Value'] == 'true' else False
                            if isKeepAlive and state['Name'] == 'running':
                                print ("DEBUG: Instance with keep alive tag ignoring")
                            else:
                                instancesToStop.append(instanceId)
                else:
                    instancesToStop.append(instanceId)

        if (len (instancesToStop) <= 0):
            print ('No Instances found to stop')
        else:
            res = ec2Client.stop_instances(
                InstanceIds = instancesToStop,
                DryRun = False
            )

        print ('~~~~~~Region {0} - End Of Day - Stopped {1} instnaces~~~~~~'.format(regionName, len(instancesToStop)))



