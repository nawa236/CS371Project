from scapy.all import *
import sys
import socket 
import os
import csv

arrayOfFlows = []
def packetSort(x):
	temp =[]
	bool = False
	if arrayOfFlows is None:
		temp.append(x)
		arrayOfFlows.append(temp)
	else:
		for p in range(len(arrayOfFlows)):
			if(x[0].type == arrayOfFlows[p][0][0].type):
				if(x[1].src == arrayOfFlows[p][0][1].src):
					if(x[1].dst == arrayOfFlows[p][0][1].dst):
						if(x[2].sport == arrayOfFlows[p][0][2].sport):
							if(x[2].dport == arrayOfFlows[p][0][2].dport):
								arrayOfFlows[p].append(x)
								bool = True
								break
		if bool == False:
			temp.append(x)
			arrayOfFlows.append(temp)



def extractFeatures(flowarray):
	length = []
	sum = 0
	min = 65535
	max = 0
	for packet in range(len(flowarray)):
		length.append(flowarray[packet][1].len)
		if flowarray[packet][1].len < min:
			min = flowarray[packet][1].len
		if flowarray[packet][1].len > max:
			max = flowarray[packet][1].len
		sum += flowarray[packet][1].len

	average = sum / len(flowarray)
	stddevsum = 0
	for l in range(len(length)):
		stddevsum += ((length[l] - average) ** 2)
	stddev = math.sqrt(stddevsum/len(length))

	with open('ips.csv', 'a') as csvfile:
        	        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL) 
	                if (flowarray[0][1].proto == 6):
        	                filewriter.writerow(['TCP', flowarray[0][2].sport, flowarray[0][2].dport, min, max, average, stddev])
                	elif (flowarray[0][1].proto == 17):
                        	filewriter.writerow(['UDP', flowarray[0][2].sport, flowarray[0][2].dport, min, max, average, stddev])



pkts = sniff(filter = 'ip', prn = packetSort, count = 5000)

for p in range(len(arrayOfFlows)):
        if len(arrayOfFlows[p]) < 1000:
                extractFeatures(arrayOfFlows[p])

