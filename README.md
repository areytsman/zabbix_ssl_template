# Zabbix SSL certs expiration check template
Template discover SSL-enabled ports on host and for each creates item with days to expire and 3 triggers with Warning, Average and High severity.

# Dependencies
* python3
* pyopenssl


# Deploy
## Zabbix server host
Place `ssl_ports_lld.py` and `ssl_expiration_check.py` in Zabbix's external scripts folder.
To find the folder you can run
```
# grep 'ExternalScripts=' /etc/zabbix/zabbix_server.conf
```
## Zabbix web interface
* Navigate to Configuration → Templates → Import and choose `Template SSL certs expiration check.xml` file in proper field. Next put `Import` button.
* Navigate to Configuration → Hosts → you_host → Templates and link the template.