import socket
from dns_server import DNS_PORT, DESTINATION

requests = {
    'vk': b"\x75\xa3\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x02\x70\x75\x02"
          b"\x76\x6b\x03\x63\x6f\x6d\x00\x00\x01\x00\x01",
    'mail': b"\x32\xec\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x02\x67\x6f\x08"
            b"\x69\x6d\x67\x73\x6d\x61\x69\x6c\x02\x72\x75\x00\x00\x01\x00\x01",
    'ulearn': b"\xcd\xbe\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03\x61\x70\x69"
              b"\x06\x75\x6c\x65\x61\x72\x6e\x02\x6d\x65\x00\x00\x01\x00\x01"}

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(2)
sock.sendto(requests['mail'], (DESTINATION, DNS_PORT))
print('Request was sent')
