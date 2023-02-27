'''This prograam is intended to both be a free to use network packet capture tool and knowledge showcase on
the concept of networking/packet capture.'''
#'socket' is the library for capturing 'Raw socket' information, which include Layers 3 (IP), 4 (TCP), and application layer information
import socket
#create an INET, raw socket
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

# receive a packet
while True:
  print s.recvfrom(65565)
