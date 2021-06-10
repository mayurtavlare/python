# Author: Mayur Tavlare
# Description: This lambda function automaticaly reboot workspacews 
# Trigger: Cloudwatch CRON
#!/bin/python
import boto3

workspaceunhealthy = []
wspace = boto3.client('workspaces', region_name="us-east-1")
response = wspace.describe_workspaces()
paginator = wspace.get_paginator('describe_workspaces')
# print(response['Workspaces'])


response_iterator = paginator.paginate()

for each_page in response_iterator:
    for each in each_page['Workspaces']:
        #print(each)
        #print(each['WorkspaceId'], each['State'])
        if each['State'] == 'UNHEALTHY':
            print(each['WorkspaceId'], each['State'])
            workspaceunhealthy.append(each['WorkspaceId'])

print("Unhealthly instance")
print(workspaceunhealthy)


#Reboot Unhealthy instance
for eachuh in workspaceunhealthy:
    responseuh = wspace.reboot_workspaces(RebootWorkspaceRequests=[
            {
                'WorkspaceId': eachuh
            }
        ]
        )
    print("Rebooting Unhealthly Workspaces")
