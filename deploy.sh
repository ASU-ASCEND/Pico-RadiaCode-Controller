#!/usr/bin/env bash 

mpremote fs cp -r radiacode :/

mpremote fs cp -r lib :/

# copy main file over 
mpremote fs cp main.py :main.py

# run main 
mpremote run main.py