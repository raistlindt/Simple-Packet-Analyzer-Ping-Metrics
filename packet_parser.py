
"""
Jack McCarthy
01/06/2021
Simple Packet Analyzer: Ping Metrics
Description: Parses the filtered packet lists and uses itemgetter to create a list out of the indexes needed for metric computation

"""
#Searches for matching echo requests and replies. If a match is found it is added to a single list as a pair.
#Each packet pair is then added to another list for the compute function.

#Indexes in packet_list 0= No. 1=time 2=source 3=destination 4=protocol 5=length(frame) 8(ping/request) 10=sequence

#Indexes in packet_collection
# 0=No. 1=time 2=source 3=destination 4=length(frame) 5(ping/request) 6=sequence 7=ttl
from operator import itemgetter
packet_collection = []
compute_list = []

def parse(nodelists):
    count = 0
    packet_collection = []
    print(len(nodelists))
    for x in range(len(nodelists)):
        for i in range(len(nodelists[x])):
            count+=1
# Itemgetter returns a tuple of selected indexes. This line also converts the tuple into a list.
            temp = list(itemgetter(0,1,2,3,5,8,10,11)(nodelists[x][i]))
            temp[7] = int(temp[7][4:])
            packet_collection.append(temp)

        compute_list.append(packet_collection)
        count = 0
        packet_collection = []
    return compute_list

