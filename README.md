# proxy-updater

usage:
python3 proxy-updater.py -t/--type [proxy type] -p/--path [path to Proxychains config file] -c/--chain [chain type]
if you won't specify arguments it will load them form config.ini file
program supports only Proxychains
avaliable proxy types: http, socks4, socks5, all
avaliable chain types: dynamic, random
