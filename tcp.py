#!/usr/bin/python

import argparse
from socket import *

def ShowBanner(ports,sock): 
                           try:
                             if ports == "80":
		                    sock.send("GET HTTP/1.1  \r\n")
		             else:
		                sock.send(" \r\n ")
		                results = sock.recv(4096)	
                                print "Running: " + str(results) + "\n"
                           except:
                                print "Service Unavailable!\n"
      
def tcpScan(targetIp,targetPort):
                         print "Working on: " + targetIp + "\n" 
                         try: 
		            sock = socket(AF_INET,SOCK_STREAM)
		            sock.connect((targetIp,int(targetPort)))
                            print "TCP Port: " +str(targetPort) + " OPEN"
                            ShowBanner(targetPort,sock) 	
                         except:
                             print "TCP Port: " +str(targetPort) + " CLOSED\n"
                         finally:
                               sock.close()

def udpScan(targetIp,targetPort):
       try:
          consock = socket(AF_INET,SOCK_DGRAM)
          consock.connect((targetIp,targetPort))
          print "UDP Port Open: " + str(targetPort)
          ShowBanner(targetPort,consock)
       except:
          print "UDP port closed: " + str(targetPort)
          
def checkType(ip,port,isUdp):
     for ports in port:
         if not(isUdp):
            tcpScan(ip,int(ports))
         else:
            udpScan(ip,int(ports))
       
def main():
    print "TCP Port Scanner!\n"
    try:
     parser = argparse.ArgumentParser("TCP Scan")
     parser.add_argument("-a","--address",type=str,help="Enter IP address to scan")
     parser.add_argument("-p","--port",type=str,help="Enter port to scan")
     parser.add_argument("-u","--udp",action="store_true")
     args = parser.parse_args()
     ipaddress = args.address
     port = args.port.split(',')
     isUdp = args.udp
    
     checkType(ipaddress,port,isUdp)
     
    except:
     print "Error \n example: tcp.py -a 192.168.43.224 -p 21,22,80"
    
main()
