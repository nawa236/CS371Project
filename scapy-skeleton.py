from scapy.all import *
import sys
import socket 
import os
import csv

def fields_extraction(x):
#	print x.sprintf("{IP:%IP.src%,%IP.dst%,}"
#        	"{TCP:%TCP.sport%,%TCP.dport%,}"
#        	"{UDP:%UDP.sport%,%UDP.dport%}")

	with open('ips.csv', 'a') as csvfile:
		filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		if (x[IP].proto == 6):
	    		filewriter.writerow(['TCP', x.sprintf('%IP.src%'), x.sprintf('%TCP.sport%'), x.sprintf('%IP.dst%'), x.sprintf('%TCP.dport%')])
		elif (x[IP].proto == 17):
			filewriter.writerow(['UDP', x.sprintf('%IP.src%'), x.sprintf('%UDP.sport%'), x.sprintf('%IP.dst%'), x.sprintf('%UDP.dport%')])
   	print x.summary()
   	x.show()

    	#use x.time for time information on the pkts

pkts = sniff(prn = fields_extraction, count = 10)
print pkts[0].show()
