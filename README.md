# Simple-Packet-Analyzer-Ping-Metrics
Computes metrics of successful pings based on packet captures converted to txt files.

This is a simple program that takes packet captures in a txt format and computes metrics about the ping utility. This program only computes metrics based on successful echo requests and replies.

The included packet capture txt files are in the Captures folder. Here is a brief description of each function.

# filter_packets.py:
	Includes the filter_packets function.
	Within this function you can adjust the path of the captures you want to filter by changing the 
	nodeTxts list. Depending on the length of the list it will filter through the txt file and 		return a list of packets that use the ping utility. It checks the 	  packet summary line to see if
	the packet type includes the string 'Echo', which is in the ping echo request and reply ICMP 		packet types.

# packet_parser.py:
	This function takes the filtered packet list of echo requests and replies and parses them for
	data that is needed in the compute_metrics function. It uses the itemgetter function to quickly
	select the indexes of the data required. After looping through the list of lists it returns the
	list of each packet summary with the necessary values for computation.

# compute_metrics.py:
	This function requires the IP address of the node in which the packet capture takes place. To
	change this edit the nodeIPs variable. You should have the same number of IP addresses in the
	list that you had in the nodeTxt variable in the filter_packets function.
		Example:
			If you are computing metrics from two packet captures the length of the nodeTxts
			list should be 2 and the nodeIPs list should be 2.

MAIN PROGRAM:

packet_analyzer.py:
	This function imports the three previous modules and runs them. It filters the packet txts,
	parses them for data and computes metrics.

This is my first attempt at creating a program and uploading it to GitHub. I'm sure there are a lot more effecient ways to perform calculations like this, and documenting the program, but this was the first idea that popped into my head. The program functions pretty well, but could be cleaned up and simplified to be more efficient. I am thinking of rewriting this program to use scapy to compute metrics based on .pcap files instead of .pcaps converted to txts. Any suggestions are welcome!
