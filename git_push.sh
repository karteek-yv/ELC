#!/bin/bash
git add .
git commit -m "$(date +"%d/%m/%Y - %T")"
git push -u git@github.com:karteek-yv/ELC.git master
