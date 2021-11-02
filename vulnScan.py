#!/usr/bin/python

import socket #Perfrom connection and receive data from target Package
import os     #Checks if files exists
import sys    #Checks out the number of arguments

def retBanner(ip,port): #Connectiong to ip and port to find banner 
        try:
                socket.setdefaulttimeout(2)
                s = socket.socket()
                s.connect((ip,port))
                banner = s.recv(1024)
                return banner
        except:
                return

def checkVulns(banner, filename): #Opening your text file full of vuln and matching it with the tartget system
        f = open(filename, "r") #This function opens the file and can perform read write append
        for line in f.readlines(): # function that reads line by line
                if line.strip("\n") in banner:
                        print('[+] Server is vulnerable: ' + banner).strip("\n")

def main():
        if len(sys.argv) == 2: #Must have 2 arguments
                filename = sys.argv[1]
                if not os.path.isfile(filename): #Checks if the file doesn't exist or isn't a file
                    print("[-] File Doesn't Exist!")
                    exit(0)
                if not os.access(filename, os.R_OK): #Check if we don't have access to the file
                    print('[-] Acces Denied!')
                    exit(0)
        else:
                print('[-] Usage: ' + str(sys.argv[0] + " <vuln filename>"))
                exit(0)
        portlist = [21,22,25,80,110,443,445]
        for x in range(128,130):
                ip = "192.168.44." + str(x)
                for port in portlist:
                        banner = retBanner(ip,port)
                        if banner:
                                print('[+] ' + ip + "/" + str(port) + " : " + banner).strip("\n")
                                checkVulns(banner, filename)
main()
