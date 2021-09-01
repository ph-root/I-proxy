# I-proxy
Mass Proxy Checker. It checks if the proxy is Up [LIVE] or Down [Dead] and Detect the Type of Proxy [HTTP / HTTPS / SOCKS4 / SOCKS5 ].

# Install

git clone https://github.com/ph-root/I-proxy.git

# Run

Usage : python3 I-proxy.py -f [file.txt] -t [type of proxies] -o [output folder]

                help:
                -f the PATH of file contains the proxies you want to check
                -t http,https,socks4,socks5 or ALL to check all types
                -o name of folder to save the output in

                EX:

                python3 I-proxy.py -f proxies.txt -t ALL -o out1
                python3 I-proxy.py -f proxies.txt -t socks5 -o out2


![alt text](https://prnt.sc/1qzn2lp)
