# Functions for managers and clients
import os
import socket
import sys
import thread

def sysStart(hostList,portNum):
    username = 'hengx19'
    for i in hostList:
    #     os.system('ssh '+ username + '@' + i + ' pwd')
         os.system('ssh '+ username + '@' + i + ' python tms.py ' +  str(portNum))


# def sysStop(command):

# def dInit():

# def dread():

# def dwrite():

# def dopen():

# def dclose():
