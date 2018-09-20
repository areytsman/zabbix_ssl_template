#!/usr/bin/python3

import ssl
import OpenSSL
import datetime
import sys


if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.exit(-1)
    host = sys.argv[1]
    port = sys.argv[2]
    if len(host) == 0:
        sys.exit(-1)

    cert = ssl.get_server_certificate((host, port))

    x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, bytes(cert.encode()))

    expire_timestamp = x509.get_notAfter().decode()
    year = int(expire_timestamp[:4])
    month = int(expire_timestamp[4:6])
    day = int(expire_timestamp[6:8])
    expire = datetime.datetime(year, month, day)
    days_to_expire = expire - datetime.datetime.now()

    print(days_to_expire.days)
