#!/usr/bin/python3
import socket
import sys
import json
import ssl
from multiprocessing.dummy import Pool
from itertools import repeat
ssl_ports = (443, 587, 636, 993, 995, 8888)

def ssl_ports_discovery(port: int, hostname: str):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3.0)
    conn = sock.connect_ex((hostname, port))
    if conn == 0:
        sock.close()
        if check_ssl(hostname, port):
            return port
    sock.close()


def check_ssl(host: str, port: int):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3.0)
    ssl_sock = ssl.SSLSocket(sock)
    try:
        ssl_sock.connect((host, port))
        ssl_sock.getpeercert()
        ssl_sock.close()
        sock.close()
        return True
    except:
        sock.close()
        return False


def make_lld_json(ports):
    dict_to_json = {'data': []}
    for port in ports:
        if port is not None:
            dict_to_json['data'].append({"{#SSLPORT}": str(port)})
    return json.dumps(dict_to_json)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(-1)
    host = sys.argv[1]
    if len(host) == 0:
        sys.exit(-1)

    pool = Pool(len(ssl_ports))
    results = pool.starmap(ssl_ports_discovery, zip(ssl_ports, repeat(host)))
    print(make_lld_json(results))
