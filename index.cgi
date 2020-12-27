#!/bin/bash

echo "Content-Type: text/html"
echo


cat header.html
cat searchbar.html

Q=$(echo "$QUERY_STRING" | sed -n 's/^.*q=\([^&]*\).*$/\1/p' | sed "s/%20/ /g; s/%2F/\//g; s/%5C/\\\/g" | sed "s/+/ /g; s/%2B/+/")

if [[ $Q ]]
then

./ebl "$Q"
./huntnw "$Q" 


[ -z $(./huntnw "$Q") ] && echo "<div class='box'>No results for $Q</div>"
else
	echo "<div class='box'>a powerful regex-based search engine for nmap results kinda like shodan</div>"
	echo "<div class='box'>$(echo index/* | wc -w) ips scanned.</div>"
	cat footer.html
fi


