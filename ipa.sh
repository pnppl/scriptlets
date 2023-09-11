#!/bin/bash
echo -en "Pronunciation: \033[1m"
python3 ~/.bin/ipa.py "$*"
echo -en "\033[0m"
