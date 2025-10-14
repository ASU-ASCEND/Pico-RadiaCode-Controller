#!/usr/bin/env bash 

mpremote fs cp -r radiacode :/radiacode

# copy main file over 
mpremote fs cp main.py :main.py

# run main 
mpremote run main.py