#!/user/bin/env bash 

# copy python files over 
mpremote fs cp main.py :main.py

# run main 
mpremote run main.py