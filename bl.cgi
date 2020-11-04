#!/bin/bash

echo "Content-Type: text/plain"
echo




Q=$(echo "$QUERY_STRING" | sed -n 's/^.*q=\([^&]*\).*$/\1/p' | sed "s/%20/ /g; s/%2F/\//g; s/%5C/\\\/g" | sed "s/+/ /g; s/%2B/+/")

if [[ $Q ]]
then

grep "$Q" bl.txt lists/* || echo "0	0	Not found in blacklist"


else

cat <<EOF
# shoxf bl
# to query this, simply use a ?q=<ip> query string
#
# shoxf bl outputs data in tsv format. a typical responce would look like:
# bl.txt:127.0.0.1
# but there is sometimes additional info after a <tab> 
#
# if any lines not starting with # are seen,
# consider it listed
#
EOF
fi


