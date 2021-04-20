#!/bin/bash

nmap -Pn -Ap 25565 $@ |
	tr "\n" "\t" | sed 's/\tNmap/\nNmap/g' |
	grep 'open' | awk -F'\t' '{print $1 "\t" $5}' |
	tee -a "minecraft.txt"



sort "minecraft.txt" | uniq > "minecraft.txt.temp"
mv "minecraft.txt.temp" "minecraft.txt"


