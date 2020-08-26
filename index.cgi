#!/bin/bash

echo "Content-Type: text/html"
echo


cat header.html


Q=$(echo "$QUERY_STRING" | sed -n 's/^.*q=\([^&]*\).*$/\1/p' | sed "s/%20/ /g; s/%2F/\//g; s/%5C/\\\/g" | sed "s/+/ /g; s/%2B/+/")

if [[ $Q ]]
then

./huntnw "$Q" 


[ -z $(./huntnw "$Q") ] && echo "<div class='box'>No results for $Q</div>"
fi

cat footer.html

