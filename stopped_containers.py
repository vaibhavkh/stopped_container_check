import docker 
from sys import exit
conn=docker.DockerClient()
TotalContainers=conn.info()['Containers']
StoppedContainer=conn.info()['ContainersStopped']
if StoppedContainer !=0:
    print("We have %s stopped containers" % StoppedContainer)
    exit(2)
else:
    print("All %s containers are running" % TotalContainers)
    exit(0)
