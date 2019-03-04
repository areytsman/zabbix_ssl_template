# Zabbix SSL certs expiration check template
Template discover SSL-enabled ports on host and for each creates item with days to expire and 3 triggers with Warning, Average and High severity.

# Dependencies
* python3
* pyopenssl


# Deploy
## Zabbix server host
* Install python3 and pip3 packages. For example (CentOS):
```
# yum install python34 python34-pip
```
N.B. python versions >= 3.7 are not supported.
* Install pyopenssl library:
```
pip3 install pyopenssl
```
* Place `ssl_ports_lld.py` and `ssl_expiration_check.py` in Zabbix's external scripts folder.
To find the folder you can run
```
# grep 'ExternalScripts=' /etc/zabbix/zabbix_server.conf
```
## Zabbix web interface
* Navigate to Configuration → Templates → Import and choose `Template SSL certs expiration check.xml` file in proper field. Next put `Import` button.
* Navigate to Configuration → Hosts → you_host → Templates and link the template.

# Settings
Change ssl_ports list in `ssl_ports_lld.py` to reflect you services. By default script check 443, 587, 636, 993, 995 and 8888 ports.

## SNI support
If you need a sni support (multiple hostnames for one IP) replace file ssl_expiration_check.py by ssl_expiration_check_sni.py
NOTE! This change will break getting an untrusted certificates (self-signed, expired etc). 
