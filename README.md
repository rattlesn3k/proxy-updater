# proxy-updater
----------------------------------------------------------------------------------------------------------------------
Run the script as root or super user, otherwise it will not apply changes to Proxychains config file
----------------------------------------------------------------------------------------------------------------------
USAGE:
python3 proxy-updater.py -t/--type [proxy type] -p/--path [path to Proxychains config file] -c/--chain [chain type]
-----------------------------------------------------------------------------------------------------------------------
If you won't specify arguments it will load them form config.ini file
Program supports only Proxychains
Avaliable proxy types: http, socks4, socks5, all
Avaliable chain types: dynamic, random
-----------------------------------------------------------------------------------------------------------------------
