#!/bin/bash

echo "Content-Type: text/html"
echo


cat header.html


Q=$(echo "$QUERY_STRING" | sed -n 's/^.*q=\([^&]*\).*$/\1/p' | sed "s/%20/ /g" | sed "s/+/ /g")

if [[ $Q ]]
then

./huntnw "$Q" 


[ -z $(./huntnw "$Q") ] && echo "<div class='box'>No results :(</div>"
fi

cat footer.html

