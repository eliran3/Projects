#! /usr/bin/python3

from scapy.all import *
import threading, netifaces
from colorama import Fore
from time import sleep

ips = []

def get_gateway():
    return netifaces.gateways()['default'][netifaces.AF_INET][0]

subdomain = get_gateway()[:len(get_gateway())-2]

stop_sniffer = threading.Event()

thread = socket = None

def get_iface():
    return netifaces.gateways()['default'][netifaces.AF_INET][1]

def sniffing():
    socket = conf.L2listen(type=ETH_P_ALL, iface=get_iface())
    sniff(prn=find_ips, opened_socket= socket, timeout=30, quiet=True, stop_filter=should_stop_sniffer, lfilter=lambda pkt: 'IP' in pkt)
    print(Fore.BLUE + 'Finished scanning!')

def should_stop_sniffer(packet):
    return stop_sniffer.isSet()

def find_ips(packet):
    if packet['IP'].src.startswith(subdomain) and packet['IP'].src not in ips:
        ips.append(packet['IP'].src)
    if packet['IP'].dst.startswith(subdomain) and packet['IP'].dst not in ips:
        ips.append(packet['IP'].dst)

def perform_ip_scan():
    global thread

    print(Fore.BLUE + 'Performing ip scan...')

    if thread is None or not thread.is_alive():
        stop = False
        thread = threading.Thread(target=sniffing)
        thread.start()

def main():
    perform_ip_scan()

    try:
        while True:
            sleep(100)
    except KeyboardInterrupt:
        stop_sniffer.set()
        
        if thread.is_alive():
            socket.close()
        
        print(Fore.BLUE + f'\n{ips}')

if __name__ == '__main__':
    main()
