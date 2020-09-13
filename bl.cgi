#!/bin/bash

echo "Content-Type: text/plain"
echo




Q=$(echo "$QUERY_STRING" | sed -n 's/^.*q=\([^&]*\).*$/\1/p' | sed "s/%20/ /g; s/%2F/\//g; s/%5C/\\\/g" | sed "s/+/ /g; s/%2B/+/")

if [[ $Q ]]
then

grep "$Q" bl.txt || echo "0	0	Not found in blacklist"


else

cat <<EOF
# shoxf bl
# to query this, simply use a ?q=<ip> query string
#
# shoxf bl outputs data in tsv format. a typical responce would look like:
# 127.0.0.1	1
# the second part is the category type
#
# category types:
# 1: abused ip
# 11: malware/botnet
# 111: DDoS drone
# 112: IRC drone
# 12: portscanning
# 2: vpn/proxy
# 21: open proxy
# 211: open socks
# 212: open http/webpage proxy
# 22: abused vpn/proxy
# 221: unknown abused vpn/proxy # (send help :p)
#
# you might notice that additional digits = sub-category :3

EOF
fi


