import socket
from optparse import OptionParser
#------------------- The Instraction-------------------------------------------#
parse = OptionParser("""
    Hello All In My Program To Cheack The Open & Close Ports 'Security'
""")
#------------------- Adding Options--------------------------------------------#
parse.add_option("-p","--port",dest="the_port",help="port_help")
parse.add_option("-o","--open",dest="open",help="hopen")
parse.add_option("-c","--close",dest="close",help="hclose")
#------------------- Parsing The Options 'res is array'------------------------#
(res, args) = parse.parse_args()
#------------------- Condition for the Ports-----------------------------------#
LIST = []
if res.the_port != None:
    while True:
        port = int(input("Please Enter The Port Number '0 for exit' : "))
        LIST.append(port)
        if port == 0:
            break
#------------------- Open Setion-----------------------------------------------#
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
for arg in LIST:
    scan = sock.connect_ex(("127.0.0.1",arg))
    if res.open != None and res.close != None:
        if scan == 0:
            print("{0} => Open".format(arg))
        elif scan != 0:
            if arg == 0:
                continue
            else:
                print("{0} => Close".format(arg))
        else:
            print("Error With Inputs")
    elif res.open != None:
        if scan == 0:
            print("{0} => Open".format(arg))
    elif res.close != None:
        if scan != 0:
            if arg == 0:
                continue
            else:
                print("{0} => Close".format(arg))
