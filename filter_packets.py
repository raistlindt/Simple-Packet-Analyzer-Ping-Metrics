
"""
Jack McCarthy
01/06/2021
Simple Packet Analyzer: Ping Metrics
Description: Filters the text files and returns a list of only ICMP echo requests and replies
"""


def filter_packets():
    nodelists = []
    nodeTxts = ['Captures/Node1.txt','Captures/Node2.txt', 'Captures/Node3.txt', 'Captures/Node4.txt']


    packet_list = []
    count = 0
    for i in range(len(nodeTxts)):
        f1 = open(nodeTxts[i], 'r')
        line = f1.readline()
        while line:
            line = line.strip()
            if 'No.' in line:
                current = next(f1, '')
                split = current.split()
                if 'Echo' in current:
                    count+=1
                    packet_list.append(split)
            line = f1.readline()
        nodelists.append(packet_list)
        packet_list = []
        f1.close()
    return nodelists


	
print('called filter function in filter_packets.py')
	
