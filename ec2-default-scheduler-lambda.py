import os
import boto3
import botocore
import json

def lambda_handler(event, context):


    ec2Client = boto3.client('ec2')

    regions = [region['RegionName'] for region in ec2Client.describe_regions()['Regions']]
    #regions = ['eu-north-1']

    for regionName in regions:
        print('~~~~~~Region:{0}~~~~~~'.format(regionName))
        ec2Client = boto3.client('ec2', region_name=regionName)
        response = ec2Client.describe_instances(MaxResults=1000)

        instancesToStop = []
        for reservations in response['Reservations']:
            instanceId = ''
            instanceName = ''
            state = ''

            for instanceDetails in reservations['Instances']:
                instanceId = instanceDetails['InstanceId']

                # ignore spot and scheduled instances
                if 'InstanceLifecycle' in instanceDetails.keys():
                    continue

                state = instanceDetails['State']
                if state['Name'] == 'running':
                    instancesToStop.append(instanceId)

                if 'Tags' in instanceDetails:
                    for tag in instanceDetails['Tags']:
                        if tag['Key'] == 'Name':
                            instanceName = tag['Value'] if not tag['Value'] else 'Instance with no name'

                        if tag['Key'] == 'KeepAlive':
                            isKeepAlive = True if tag['Value'].lower() == 'true' else False
                            if isKeepAlive:
                                print ('Instance {0} with keep alive tag -> ignoring'.format(instanceName))
                                instancesToStop.remove(instanceId)

        if (len (instancesToStop) <= 0):
            print ('No Instances found to stop')
        else:
            res = ec2Client.stop_instances(
                InstanceIds = instancesToStop,
                DryRun = False
            )

        print ('~~~~~~Region {0} - End Of Day - Stopped {1} instnaces~~~~~~'.format(regionName, len(instancesToStop)))
