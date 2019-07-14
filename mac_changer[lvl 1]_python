#!/usr/bin/env python3
import optparse
import subprocess
import random


def parsing():
    parser = optparse.OptionParser()
    parser.add_option('-i', "--interface", dest="Interface", help="The name of the net card")
    parser.add_option('-m', "--mac", dest="MAC", help="the number that we want it to replace")
    parser.add_option('-g', "--Generate", dest="RandomMAC", help="helps you to generate random MAC numbers")
    return parser.parse_args()


def generate(number):
    for i in range(number):
        mac = ''
        for j in range(0, 12):
            if j % 2 == 0 and j != 0:
                mac += ':'
            rand = int(random.random() * 16)
            if rand > 9:
                rand = 55 + rand
                mac += str(chr(rand))
            else:
                mac += str(rand)
        print(mac)


(values, args) = parsing()
interface = values.Interface
MAC = values.MAC
GenerateRandomMAC = values.RandomMAC

if interface and MAC:
    print(f"[!] The new MAC is : [{MAC}] for interface : [{interface}] would you want to continue ? (y/n)")
    accept = input()
    if accept.lower() == 'y':
        print("[!] Waiting...")
        print("[+] Start changing MAC Address.")
        subprocess.call(["ifconfig", interface, "down"])
        print(f"[+] [{interface}] was down.")
        subprocess.call(f"ifconfig {interface} hw ether {MAC}.", shell=True)
        print(f"[+] [{interface}] was changed to new MAC address : [{MAC}]")
        subprocess.call(["ifconfig", interface, "up"])
        print(f"[+] [{interface}] is up now.")
        print(f"[+] Done Successfully !")
        print("""
        Developed By : 0X1999 => Abdelrahman Saleh [Robot]
        """)
    else:
        print("[-] Access Denied !")
else:
    if GenerateRandomMAC:
        if int(GenerateRandomMAC) > 0:
            generate(int(GenerateRandomMAC))
        else:
            generate(1)
    elif not interface:
        print("[-] Hey bro, you missed the -i option then the card name.")
    elif not MAC:
        print("[-] Hey bro, you missed the -m option then the number of new MAC.")


