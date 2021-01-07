from filter_packets import *
from packet_parser import *
from compute_metrics import *

"""
Jack McCarthy
01/06/2021
Simple Packet Analyzer: Ping Metrics
Description: Incorporates three functions to filter, parse, and compute metrics of the packet captures. 
Output is displayed in the terminal and output.csv
"""
nodelists = filter_packets()
compute_list = parse(nodelists)
compute(compute_list)
