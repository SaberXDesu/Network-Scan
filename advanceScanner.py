#!/usr/bin/python

from socket import *
import optparse #This library specifies the help option that we get prompted to the uesr. E.g., -h for help
from threading import * 


def connScan(tgtHost, tgtPort):
        try:
                sock = socket(AF_INET, SOCK_STREAM) #Notice that we there is not socket.AF_INET, socket.socket? This is because of "from socket import *"
                sock.connect((tgtHost,tgtPort))
                print('[+] %d/tcp Open'%(tgtPort))
        except:
                print('[-] %d/tcp Closed'%(tgtPort))
        finally:
                sock.close()

def portScan(tgtHost,tgtPorts): #Resolving DNS to IP
        try:
                tgtIP = gethostbyname(tgtHost) #Get IP from DNS
        except:
                print("Unknown Host %s"%(tgtHost))#Unknown host from DNS
        try:
                tgtName = gethostbyaddr(tgtIP) #Get DNS
                print('[+] Scan Results for: ' + tgtName[1])
        except:        
                print('[+] Scan Results for: ' + tgtIP)
        setdefaulttimeout(1)
        for tgtPort in tgtPorts:
                t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
                t.start()

def main():
        parser = optparse.OptionParser('Usage of program: ' + '-H <target host> -P <target port>')
        parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
        parser.add_option('-P', dest='tgtPort', type='string', help='specify target ports seperated by comma')
        (options, args) = parser.parse_args()
        tgtHost = options.tgtHost
        tgtPorts = str(options.tgtPort).split(',')
        if (tgtHost == None) | (tgtPorts[0] == None):
            print(parser.usage)
            exit(0)
        portScan(tgtHost,tgtPorts)

if __name__== '__main__':
    main()
