"""
Jack McCarthy
01/06/2021
Simple Packet Analyzer: Ping Metrics
Description: Takes the parsed lists as an argument and returns metrics to both the terminal and output.csv
"""

def compute(compute_list):
    nodeIPs = ['192.168.100.1','192.168.100.2','192.168.200.1','192.168.200.2']
    print(len(compute_list))
    for x in range(len(compute_list)):
        all_data= compute_list[x]
        IP = nodeIPs[x]
        reqSent = 0
        reqRecv = 0
        repSent = 0
        repRecv = 0
        totalReqSentFrameSize = 0
        totalReqRecvFrameSize = 0
        totalReqSentData = 0
        totalReqRecvData = 0
        RTTtemp = -1
        totalRTT = 0
        delayTemp = -1
        totalDelay = 0
        hopTemp = -1
        totalHop = 0

# 0/7=No. 1/8=time 2=source address 3=destination address 4=length(frame) 5(ping/request)
# 6=sequence number 7=ttl

        for data in all_data:
             
            if data[2] == IP:  # Sent Frames
                
                if data[5] == "request":  # Sent request Frames
                    reqSent += 1
                    totalReqSentFrameSize += int(data[4])
                    totalReqSentData += int(data[4]) - 42
                    hopTemp = data[7]
                    RTTtemp = float(data[1])

                elif data[5] == "reply":  # Sent reply Frames
                    repSent += 1
                    if delayTemp != -1:
                        totalDelay += float(data[1]) - delayTemp
                        delayTemp = -1
            elif data[3] == IP: # Recv Frames
                if data[5] == "request":  # Recv request Frames
                    reqRecv += 1
                    totalReqRecvFrameSize += int(data[4])
                    totalReqRecvData += int(data[4]) - 42
                    delayTemp = float(data[1])
                elif data[5] == "reply":  # Recv reply Frames
                    repRecv += 1
                    if RTTtemp != -1:
                        totalRTT += float(data[1]) - RTTtemp
                        RTTtemp = -1
                    if hopTemp != -1:
                        totalHop += hopTemp - int(data[7]) + 1
                        hopTemp = -1
        avgRTT = totalRTT / repRecv * 1000
        throughput = totalReqSentFrameSize / totalRTT /1000
        goodput = totalReqSentData / totalRTT / 1000
        avgDelay = totalDelay / repSent * 1000000
        avgHop = totalHop / repRecv
        nodeVal=x+1

#Creates a CSV of metrics
        output = open("output.csv", "a")
        output.write("Node " + str(nodeVal))
        output.write('\n\n')
        output.write("Echo Requests Sent,Echo Request Received,Echo Replies Sent,Echo Replies Received,\n")
        output.write(str(reqSent)+","+str(reqRecv)+","+str(repSent)+","+str(repRecv)+"\n")
        output.write("Echo Request Bytes Sent (bytes),Echo Request Data Sent (bytes)\n")
        output.write(str(totalReqSentFrameSize)+","+str(totalReqSentData)+"\n")
        output.write("Echo Request Bytes Received (bytes),Echo Request Data Received (bytes)\n")
        output.write(str(totalReqRecvFrameSize)+","+str(totalReqRecvData)+"\n")
        output.write('\n')
        output.write("Average RTT (milliseconds),"+str(round(avgRTT,2))+"\n")
        output.write("Echo Request Throughput (kB/sec),"+str(round(throughput,1))+"\n")
        output.write("Echo Request Goodput (kB/sec),"+str(round(goodput,1))+"\n")
        output.write("Average Reply Delay (microseconds),"+str(round(avgDelay, 2))+"\n")
        output.write("Average Echo Request Hop Count,"+str(round(avgHop, 2))+"\n")
        output.write('\n')

#Returns metrics to terminal window.
        print("Node " + str(nodeVal) +" Results:")
        print()
        print("Echo Requests Sent: " + str(reqSent))
        print("Echo Requests Received: " + str(reqRecv))
        print("Echo Reply Sent: " + str(repSent))
        print("Echo Reply Received: " + str(repRecv))
        print("Echo Request Bytes Sent: " + str(totalReqSentFrameSize))
        print("Echo Request Bytes Received: " + str(totalReqRecvFrameSize))
        print("Echo Request Data Sent: " + str(totalReqSentData))
        print("Echo Request Data Received: " + str(totalReqRecvData))
        print("Average RTT (ms): " + str(round(avgRTT,2)))
        print("Echo Request Throughput (kB/sec): " + str(round(throughput,1)))
        print("Echo Request Goodput (kB/sec): " + str(round(goodput,1)))
        print("Average Reply Delay (us): " + str(round(avgDelay, 2)))
        print("Average Echo Request Hop Count: " + str(round(avgHop, 2)))
        print()

