#!/usr/bin/env python
import scapy.all as scapy
import optparse
print("Welcome in => Scanner.py <=")
print("Developed By: 0X1999 => Abdelrahman Saleh [ Robot ]")
parser = optparse.OptionParser()
parser.add_option('-t', "--target", dest="target", help="IP or IP range like => '10.10.10.10/24'")
(value, args) = parser.parse_args()


def scan_my_ip(ip):
    # devices_list = []
    #  ARP Request is send the broadcast message to check who has that ip  #
    print("[ + ] Please Wait.....")
    arp_request = scapy.ARP(pdst=ip)  # Contain an ARP Request data but the destination 'target' is [ip]
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')  # The broadcast value, [ dst ] is the destination 'target'
    final_package = broadcast/arp_request  # Our package
    answered = scapy.srp(final_package, timeout=3, verbose=False)[0]  # srp => Send, Receive Package and it's list
    # timeout means if time to respond > timeout, kill task and close the program or the program will go infinitely
    # verbose=False ==> to hide the "Finish" title
    print("-------------------------------------------")
    print("    IP\t\t\t  MAC Address")
    print("===========================================")
    for element in answered:
        # Each element is also list. So, final_result is 2D list, and answered is list in it
        print("  " + element[1].psrc + "            " + element[1].src)
        # devices_list.append({"mac": element[1].src, "ip": element[1].psrc})
        # This Package has 2 values [answered, unanswered] and each value has also 2 values [request, respond]
    print("\n\n[ + ] Done Successfully !")
    # print(devices_list)
# in element[1], there are many data like [ hwsrc ], [ hwdst ], [ psrc ], [ pdst ]
# if i want to print the value of [ hwsrc ] ||>> "hard ware source or Source MAC" in 'element[0]',
# just write "print(element[1].hwsrc)" or element[1].pdst, or if you want with [ request ] ||>> "print(element[0].psrc)"


if value.target:
    scan_my_ip(value.target)
else:
    print("[ - ] Hey bro, you have missed -t or --target then IP or IP/range.")
