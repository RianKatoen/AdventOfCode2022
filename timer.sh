#!/bin/bash
for i in {01..15}
do
   time /usr/local/bin/python3.11 day$i/puzzle.py
done