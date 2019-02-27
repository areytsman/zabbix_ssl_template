#!/usr/bin/python3

import ssl
import OpenSSL
import datetime
import sys
import socket


def get_cert(hostname, port):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as sslsock:
            der_cert = sslsock.getpeercert(True)
    # from binary DER format to PEM
    pem_cert = ssl.DER_cert_to_PEM_cert(der_cert)
    return pem_cert


if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.exit(-1)
    host = sys.argv[1]
    port = sys.argv[2]
    if len(host) == 0:
        sys.exit(-1)

    cert = get_cert(host, port)

    x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, bytes(cert.encode()))

    expire_timestamp = x509.get_notAfter().decode()
    year = int(expire_timestamp[:4])
    month = int(expire_timestamp[4:6])
    day = int(expire_timestamp[6:8])
    expire = datetime.datetime(year, month, day)
    days_to_expire = expire - datetime.datetime.now()

    if days_to_expire.days >= 0:
        print(days_to_expire.days)
    else:
        print(0)
