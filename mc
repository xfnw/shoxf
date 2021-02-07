#!/bin/bash

nmap -Pn -Ap 25565 $@ |
	tr "\n" "\t" | sed 's/\tNmap/\nNmap/g' |
	grep 'open' | awk -F'\t' '{print $1 "\t" $5}' |
	tee -a "index/minecraft.txt"



sort -V "index/minecraft.txt" | uniq > "index/minecraft.txt.temp"
mv "index/minecraft.txt.temp" "index/minecraft.txt"


